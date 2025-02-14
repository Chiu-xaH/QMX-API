// api/jsExec.js
const { get_sign } = require('./get_sign');

module.exports = (req, res) => {
  const { data } = req.query; // 从请求中获取传递的 `data`

  if (!data) {
    return res.status(400).json({ error: 'Missing data parameter' });
  }

  try {
    const sign = get_sign(data); // 调用 get_sign 函数
    res.status(200).json({ sign });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
