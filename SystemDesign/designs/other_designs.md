# Other Designs

## Designing Typehead Suggestion
**Data Structure**:\
Trie

**Optimizations**:
1. How to find top suggestions:\
We could keep track of the number of searches terminated at each node.
2. How to speed up the search time:\
Storing the top suggestions at higher nodes could definitely speed up searches. However, it comes at a cost of extra storage. We could optimize the storage by 
storing only the reference to the terminal nodes rather than the entire string. To find the suggestion term, we need to traverse the tree bottom up back to the parent node.
3. How to update the trie:\
Updating the trie online is extremely costly. We could try to update the trie offline after a certain interval. One solution is to use Map-Reduce to run through the logs
and calculate the count for each word.Then, we could take a snapshot of the current trie, update with the processed data and replace the old trie.
4. How to update the frequency of terms in the trie:\
Keeping all the past counts could to cause failure in reflecting the most up to date search results. Instead, we could keep track of the Exponential Moving Average (EMA)
to reflect the most up-to-date search results.

**Storage**:\
We can take a snapshot of the trie and store it in files. The snapshot should include a level-by-level scan starting from the root node and the node information including:
* Character it holds
* Children nodes

## Designing Web Crawler
**Workflow**
1. Pick a URL from the unvisited URL list
2. Determine the IP address of its host name
3. Establish a connection with the host to download the corresponding document
4. Parse the document contents to look for new URLs
5. Add the new URLs to the unvisited URL list
6. Continue to process and store the document
7. Go back to step 1

**Components**
* URL frontier: store the list of URLs to download and decide the ordering to crawl these pages
* HTML fetcher: retrieve a web page from the server
* Extractor: extract link from the HTML documents
* Duplicate Eliminator: make sure the same content is not extracted twice
* Datastore: store retrieved pages, url and other metadata
![image](https://user-images.githubusercontent.com/30107576/98054215-35af4400-1def-11eb-87ba-ed7da7e39dcd.png)

**Document Input Stream**\
DIS is an input stream that caches the entire content of document read from the internet and provide methods to re-read the document. Each worker thread has an asscoiated 
DIS, which it reuses from document to document.

**Document Dedupe Test**\
To perform the test, we can calculate a 64-bit checksum of every processed document and store it in the database. For every new document, we could compare its checksum
to that of all the documents that have been seen before.

## Design TicketMaster
**Handle Active Reservations**\
We could have a dameon thread to handle all the active reservations. The thread need to:
1. Append new reservations
2. Remove any cancelled reservations
3. Remove any reservations with expired time

Linked HashMap is a good data structure to use as it allows for tracking the time order of the reservations and supports jumping to any specific reservations to remove it.

**Concurrency**\
Handling concurrency is important here as there could have multiple users trying to book for one empty slot. We can use transactions in SQL to avoid any clashes. For example, if we are using an SQL server we can utilize Transaction Isolation Levels to lock the rows before other threads trying to access it.
