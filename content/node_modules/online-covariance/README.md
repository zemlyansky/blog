# online-covariance
Covariance calculation (piece-by-piece)
Based on online algorithm from [wiki](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online)

## Usage
Use a parameter `ddof: 1` to calculate sample covariance, `ddof: 0` (default) - to get population covariance

```
const Cov = require('online-covariance')
const cov = Cov({ddof: 1})

const a = [1, 3, 2, 5, 8, 7, 12, 2, 4]
const b = [8, 6, 9, 4, 3, 3, 2, 7, 7]

a.forEach((x, i) => { cov(x, b[i]) })

console.log('Unbiased covariance: ', cov()) // -> -8.069
```
