const { exec, spawn } = require('child_process');
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
    
    console.log('✅ Telegram UserBot process started in background');
    
    // Response untuk HTTP request
    res.status(200).json({
      status: 'success',
      message: 'Telegram UserBot is running!',
      timestamp: new Date().toISOString(),
      environment: process.env.NODE_ENV || 'production',
      credentials_loaded: !!process.env.API_ID && !!process.env.API_HASH && !!process.env.PHONE_NUMBER
    });
    
  } catch (error) {
    console.error('❌ Error starting bot:', error);
    res.status(500).json({
      status: 'error',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
};

// Auto ping untuk keep alive (hanya jalan di server)
if (process.env.VERCEL_URL) {
  console.log('🔧 Setting up auto-ping for keep alive...');
  
  setInterval(() => {
    const url = `https://${process.env.VERCEL_URL}/api/keep-alive`;
    console.log(`🔄 Auto-pinging: ${url}`);
    
    http.get(url, (resp) => {
      console.log(`✅ Keep-alive ping response: ${resp.statusCode}`);
    }).on('error', (err) => {
      console.error(`❌ Keep-alive ping error: ${err.message}`);
    });
  }, 300000); // Ping every 5 minutes
}

// Handle process exit
process.on('SIGTERM', () => {
  console.log('🛑 Process terminated');
  process.exit(0);
});

process.on('SIGINT', () => {
  console.log('🛑 Process interrupted');
  process.exit(0);
});
