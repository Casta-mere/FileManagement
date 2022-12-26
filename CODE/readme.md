## Functions

| category        | function | stat    |
| :-------------- | :------- | :------ |
| basic           | cd       | &check; |
| basic           | tree     | &check; |
| basic           | exit     | &check; |
| basic           | clear    | &check; |
| basic           | login    | &check; |
| basic           | logout   | &check; |
| dir manipulate  | mkdir    | &check; |
| dir manipulate  | rmdir    | &check; |
| file manipulate | touch    | &check; |
| file manipulate | rm       | &check; |
| file manipulate | mv       | &cross; |
| file manipulate | cp       | &cross; |
| file manipulate | cat      | &cross; |
| file manipulate | vi       | &cross; |
| file manipulate | echo     | &cross; |
| file manipulate | find     | &cross; |
| file manipulate | chmod    | &check; |



## permission

| code  | binary |  read   |  write  | execute |
| :---: | :----: | :-----: | :-----: | :-----: |
|   0   |  000   | &cross; | &cross; | &cross; |
|   1   |  001   | &cross; | &cross; | &check; |
|   2   |  010   | &cross; | &check; | &cross; |
|   3   |  011   | &cross; | &check; | &check; |
|   4   |  100   | &check; | &cross; | &cross; |
|   5   |  101   | &check; | &cross; | &check; |
|   6   |  110   | &check; | &check; | &cross; |
|   7   |  111   | &check; | &check; | &check; |