const { spawn } = require('child_process');
const http = require('http');

module.exports = async (req, res) => {
  console.log('🔄 Starting Telegram UserBot...');
  
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }
  
  try {
    // Jalankan Python bot sebagai background process
    const pythonProcess = spawn('python', ['bot.py'], {
      detached: true,
      stdio: 'ignore'
    });
    
    pythonProcess.unref();
    
    console.log('✅ Telegram UserBot process started');
    
    // Response untuk HTTP request
    res.status(200).json({
      status: 'success',
      message: 'Telegram UserBot is running!',
      timestamp: new Date().toISOString(),
      environment: process.env.NODE_ENV || 'production'
    });
    
  } catch (error) {
    console.error('❌ Error starting bot:', error);
    res.status(500).json({
      status: 'error',
      message: error.message
    });
  }
};

// Auto ping untuk keep alive
if (process.env.VERCEL_URL) {
  setInterval(() => {
    http.get(`https://${process.env.VERCEL_URL}/api/keep-alive`);
  }, 300000); // 5 minutes
}
