module.exports = function (params) {
  if (!params) params = {}

  var meanx = 0
  var meany = 0
  var C = 0 // co-moment
  var n = 0
  var ddof = params.ddof || 0
  var cov = 0

  return function (x, y) {
    if (!isNaN(x) && !isNaN(y)) {
      if (typeof x !== 'number') {
        x = parseFloat(x)
      }
      if (typeof y !== 'number') {
        y = parseFloat(y)
      }
      var dx = x - meanx
      n += 1
      meanx += dx / n
      meany += (y - meany) / n
      C += dx * (y - meany)
      if (n > 1) {
        cov = C / (n - ddof)
      }
    }
    return cov
  }
}
