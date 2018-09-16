const test = require('tape')
const Cov = require('./index.js')

const a = [1, 3, 2, 5, 8, 7, 12, 2, 4]
const b = [8, 6, 9, 4, 3, 3, 2, 7, 7]

test('Simple sample covariance', (_) => {
  const cov = Cov({ddof: 1})
  a.forEach((ax, i) => { cov(ax, b[i]) })
  console.log(cov())
  _.true((cov() - (-8.069)) < 0.001)
  _.end()
})

test('Simple population (biased) covariance', (_) => {
  const cov = Cov({ddof: 0})
  a.forEach((ax, i) => { cov(ax, b[i]) })
  console.log(cov())
  _.true((cov() - (-7.172)) < 0.001)
  _.end()
})
