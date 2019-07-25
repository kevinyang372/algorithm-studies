# Create a class LightString to manage a string of lights, each of which has a value 0 or 1 indicating whether it is on or off.

# class LightString {
#     public LightString(int numOfLights) {
#     }

#     /**
#     * Return if the i-th light is on or off. 
#     */
#     public boolean isOn(int i) {
#     }

#     /**
#     * Switch state (turn on if it's off, turn off if it's on) of every light in the range [start, end].
#     */
#     public void toggle(int start, int end) {
#     }
# }
# Example:

# LightString str = new LightString(5); // all lights are initially off
# str.isOn(0); // false
# str.isOn(1); // false
# str.isOn(2); // false
# str.toggle(0, 2);
# str.isOn(0); // true
# str.isOn(1); // true
# str.isOn(2); // true
# str.isOn(3); // false
# str.toggle(1, 3);
# str.isOn(1); // false
# str.isOn(2); // false
# str.isOn(3); // true
# Follow-up
# Can you do better than O(n) for update?

class LightString:

    def __init__(self, num):
        self.light = [0] * num

    def isOn(self, x):
        return self.light[x] == 1

    def toggle(self, start, end):

        for i in range(start, end + 1):
            self.light[i] ^= 1