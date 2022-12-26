## Functions

| category        | function | stat    |
| :-------------- | :------- | :------ |
| basic           | cd       | &check; |
| basic           | tree     | &check; |
| basic           | exit     | &check; |
| basic           | clear    | &check; |
| basic           | login    | &check; |
| basic           | logout   | &check; |
| basic           | pw       | &check; |
| dir manipulate  | mkdir    | &check; |
| dir manipulate  | rmdir    | &check; |
| file manipulate | touch    | &check; |
| file manipulate | rm       | &check; |
| file manipulate | mv       | &check; |
| file manipulate | cp       | &check; |
| file manipulate | cat      | &check; |
| file manipulate | vi       | &cross; |
| file manipulate | echo     | &check; |
| file manipulate | find     | &check; |
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