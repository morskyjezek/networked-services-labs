# Useful OpenRefine functions for transforming LoC JSON

## Title

```
value.parseJson()['item']['title']
```

## Notes (multiple values from array)

```
forEach(value.parseJson().item.notes, v, v).join(\"| \")
```

## Item ID (LoC ID)

```
value.parseJson().item.id
```

## Medium / Format 

```
value.parseJson().item.medium[0]
```

## Item Summary 

```
value.parseJson().item.summary
```

## Parse & cleanup multiple subject headings 

```
forEach(value.parseJson().item.item.subject_headings, v, v.chomp(\".\")).join(\"; \")
```

## Creators (extract & join multiple values from an array)

```
forEach(value.parseJson().item.item.creators, v, v.title+\", \"+v.role).join(\"; \")
```


## PartOf data

```
value.parseJson().item.item.part_of
```

## Contributors (similar to Creators) 

```
forEach(value.parseJson().item.item.contributors, v, v.chomp(\".\")).join(\"; \")
```

## Repository

```
value.parseJson().item.repository[0]
```

## Rights

```
value.parseJson().item.rights_information
```