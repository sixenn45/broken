const { exec } = require('child_process');
const http = require('http');

module.exports = async (req, res) => {
  console.log('🔄 Keeping bot alive...');
  
  // Jalankan Python bot (background process)
  exec('python bot.py &', (error, stdout, stderr) => {
    if (error) {
      console.error(`❌ Error: ${error}`);
      return;
    }
    console.log(`✅ Bot process started`);
  });
  
  // Response untuk HTTP request
  res.status(200).json({
    status: 'success',
    message: 'Telegram UserBot is running!',
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
};

// Auto ping setiap 10 menit untuk keep alive
if (process.env.VERCEL_URL) {
  setInterval(() => {
    console.log('🔄 Auto-pinging to keep alive...');
    http.get(`https://${process.env.VERCEL_URL}/api/keep-alive`, (resp) => {
      console.log(`✅ Keep-alive ping response: ${resp.statusCode}`);
    }).on('error', (err) => {
      console.error(`❌ Keep-alive ping error: ${err.message}`);
    });
  }, 600000); // 10 minutes
}
