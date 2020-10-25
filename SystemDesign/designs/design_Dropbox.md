# Dropbox

## Requirements
1. Users could upload and download files.
2. Some of the uploaded files could be big (~1 GB).
3. Users should be able to see updates to files across different platforms (mobiles, pc, etc)
4. Users should be able to share data with other users.
5. Offline editing.

## Constraints
* Consistency is key. We should expect the content to be always consistent across platforms.
* Reliability is also important.
* Availability could take a hit. It is okay to not be able to visit the file for a short period of time.
* We should expect approximately the same proportion of read and write requests.
* Read and write traffic could be heavy due to file size.

## Capacity Estimation
Assumptions:
* 1M active users
* Each user upload 1 file on average.
* The average file size will be approximately 10 MB.
* Read and write traffic is approximately the same.

Storage:
1M * 1 * 10 MB = 10 TB / day

## High Level Design
![image](https://user-images.githubusercontent.com/30107576/97100696-648d2380-1653-11eb-9172-3ea2469cf62b.png)
            
## Component Design

### Client
Due to the expected large file size, we could optimize the traffic by breaking one file into several blocks. When a file is updated locally, we could calculate the diff
between the current and old version to decide which block is going to be uploaded to the server to reflect changes. The size of each block could be decided by:
* The average file size.
* The bandwidth and latency requirements.
* Storage device (optimize for space utilization)

We could also keep a local version of the metadata to capture user changes first before uploading to the remote server. This will also help enable offline functionalities.

Based on the discussion above, we could create four key components for the local client
1. Local Metadata Database:\
This is responsible for storing the key information of each file like filenames, the blocks that correspond to the files and their contents.
2. Chunker:\
Chunker helps to split a newly created file into smaller chunks and reconstruct files for read from chunks. It should also detect changes in files to determine which chunks need to be updated remotely.
3. Watcher:\
Watcher detects the update from servers via long pulling and notifies indexer for the received events.
4. Indexer:\
Indexer receives updates from watcher and applies them to the local files. It also communicates with the Synchronization server for updates in local files.

**How should clients handle slow servers?**\
For slow servers, the client should exponentially back-off (if the server is busy, delay retries and this delay should increase exponentially).

### Metadata Database
Metadata Database should maintain the following information:
* Files
* Chunks information (locations...)
* File versioning
* Workspaces / Folders
* Devices
* Users

Given the requirements on ACID, we could use MySQL which supports it by default or NoSQL databases with additional enforcement on ACID.

### Synchronization Server
Synchronization server is responsible for broadcasting changes in one client to all subscribed devices. It should also ensure the local versioning of the file is consistent with the remote versioning.
To ensure a secure and scalable communication protocol between the server and clients, it can use a Messaging Queue middleware to manage the pulling and pushing of information and balance the load.

Messaging Queue Service should:
* Support asynchronous communication between client and server.
* Store any number of requests in a scalable and reliable fashion.
* Implement two types of Queues: Request Queue (For updating the remote database) and Response Queue (For synchronizing the local database)
* Although we only need one global Request Queue, each subscribed client should have a corresponding Response Queue to make sure the message is not consumed by other clients.
![image](https://user-images.githubusercontent.com/30107576/97100833-f8132400-1654-11eb-9929-72c13a969a6d.png)

### Chunk Server
Chunk server manages the upload and download of file contents. It is separated from metadata so that the file storage could happen either in the cloud or in house.

## Overall Workflow
1. Client A updates the chunk.
2. The changes are synchronized to the remote server. The metadata is updated and changes are submitted to file storage system.
3. Client A receives confirmation and nofitications are sent to clients B and C.
4. Client B and C receives metadata updates and applies them locally.

## Metadata Partitioning
Below we present three possible partitioning strategies:
1. Vertical Partition:\
Vertical Partition divides data by its functionality/feature groups. For example, the user table could be stored in a different server compared to the file table.
Problems: 1) We may still need further partition if there are millions of rows. 2) Joining could be very expensive.

2. Range-based Partition:\
Partition based on the first letter of the filename or username.
Problems: 1) This could lead to unbalanced partitioning as E could have many more records than Z for example.

3. Hash-based Partition:\
Take the hash of the file_id or user_id and then determine which partition a record should go to. There could exist a problem of redistribution with additional servers but that could be solved with Consistent Hashing.
