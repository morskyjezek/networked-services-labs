# Exercises with regex

To review, use parentheses to create groups. This can be 
useful for referring to a sequence of characters, for example if
it occurs a certain number of times, if it doesn't occur, or if it 

## Test string

```
My number is 734-764-1817.
Or (734) 764-1817 (phone)
734 746-1817 (fax)
123-567-1839
+1 123-567-1839
(202) 388-6389

librarian@library.org
marian@rivercity-library.net
librarian@library-carpentry.net
superman@sheroes.net
superwoman@sheroes.net

http://www.librarycarpentry.org
http://www.library-carpentry.net 
https://www2.librarycarpentry.com

Computer programming
Libraries--Computer programs--Customizing
```

## Exercises

1. What would match both `superman` and `superwoman`?
1. How would you match phone number patterns? Can you account for the presence/absence of parentheses around the area code (first three numbers)? Can you add groups so that group 1 is the area codes, group 2 is the rest of the number?
1. What would match the URLs? Can you pull apart the URLs using groups?
1. Why would you want to do any of the above? Use cases? 

## Solutions

1. super(wo)?man
1. Phone numbers. No groups: `\(?\d{3}\)?-? ?\d{3}-\d{4}`; with groups: `\(?(\d\d\d)\)?-? ?(\d{3}-\d{4})`
1. URLs. No groups: `https?:\/\/www\..*\.com`; with groups: `(http|https)(:\/\/)(\w*)\.(.*)\.(org|net|com|edu)`

## Additional resources

* [Regex101](https://regex101.com/)
* [Regex crosswords](https://regexcrossword.com/challenges/beginner/puzzles/1)
* Lots of good stuff at [RexEgg](https://www.rexegg.com/), including a [section on file renaming](https://www.rexegg.com/regex-uses.html#opus)