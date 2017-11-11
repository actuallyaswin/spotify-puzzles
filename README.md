# Spotify Puzzle

Code written to work for Python 2.7 because that's what the website requested.

## 1 Reversed Binary Numbers (Difficulty Level: Easy)

```python
print(int('{0:b}'.format(int(raw_input().strip()))[::-1],2))
```
* First, we take the user's input via `raw_input()`, stripping any whitespace before or after.
* The input is then converted to an integer and fed to the `format()` function to convert the input to a binary string (notably with no leading zeros).
* The binary string is reversed using a negative step index slicing (`[::-1]`), and then converted back to an integer from base-2.

## 2 Zipf’s Song (Difficulty Level: Medium)

```python
n, k = map(int, raw_input().strip().split(' '))
for j in [i[1] for i in sorted([(lambda (a,b): [int(a)*(1 - 1./(i+1)),b])(raw_input().strip().split(' ')) for i in range(n)])[::-1][:k]]:
	print(j)
```
* We first take the user's input via `raw_input()`, stripping any whitespace before or after, and splitting the input on whitespace.
* The `map()` function converts the split strings into integers, storing them in *n* and *k*, respectively. Here, *n* represents the number of songs in the album, and *k* represents the number of "top songs" we'd like to print out.
* Next, we loop over `range(n)` with index *i* and take in *n*-number of `raw_input()`s, which are additionally stripped and split over whitespace. The first value of the split string is the popularity value of the song, and the second value of the split is the song name. These two values will get mapped to *a* and *b*, respectively, in the wrapping `lambda()` function.
* The `lambda()` function takes *a* and *b* from the user's input and reformats them into a new list, where the first element is `int(a)*(1 - 1./(i+1))` and the second element is just *b* (i.e. the song title). This first element is crucial, as it computes the song's true popularity value as influenced by Zipf’s Law. If the provided popularity value is *a*, then the true value would be *(a - a/i)*, where *i* is the song number starting from 1. I factored out *a* and re-wrote this quanity as `int(a)*(1 - 1./(i+1))`. The use of the period after the 1 in the numerator is significant, because this ensures that the division returns a float.
* This program thus creates a new internal list which is a unsorted list of song names and their true popularity values using Zipf’s Law.
* We use Python's native `sorted()` function to sort our the internal list based on true popularity. Even though the `sorted()` function supports reversing using a named parameter, I chose to once agani use negative step index slicing (`[::-1]`).
* The `[:k]` indexing cuts the list so that only the top *k* items remain.
* We construct an new anonymous list using the second elemement of the above list, to only retrieve the song names and to ignore the computed popularitiy value. This is done using the outermost list comprehension with the `i[1]` parameter.
* Lastly, we loop through this list of *k* song names using iterator *j* and print out the song names.

I did not see a way to make this a one-liner, as there are two different types of inputs, so they need to be taken in and processed separately.

Also, from what I understand, Python2 returns an error when calling the `print()` function within a list comprehension, therefore the last for-loop is written explicitly. However, in Python3, this solution could be condensed down to two lines.