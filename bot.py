const { spawn } = require('child_process');

module.exports = async (req, res) => {
  console.log('🔄 Starting Telegram UserBot...');
  
  // Cek environment variables
  if (!process.env.API_ID || !process.env.API_HASH || !process.env.PHONE_NUMBER) {
    return res.status(200).json({
      status: 'warning',
      message: 'Environment variables not set! Please setup API_ID, API_HASH, and PHONE_NUMBER.',
      timestamp: new Date().toISOString()
    });
  }
  
  try {
    console.log('✅ Environment variables loaded');
    
    // Hanya response success, JANGAN jalanin bot.py di serverless
    // Karena Telethon butuh persistent session
    res.status(200).json({
      status: 'success',
      message: 'Bot configuration is ready! (Bot runs via GitHub Actions)',
      timestamp: new Date().toISOString(),
      environment: 'Vercel Serverless'
    });
    
  } catch (error) {
    console.error('❌ Error:', error);
    res.status(200).json({
      status: 'error',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
};

// Auto ping untuk keep alive
if (process.env.VERCEL_URL) {
  setInterval(() => {
    require('http').get(`https://${process.env.VERCEL_URL}/api/keep-alive`);
  }, 300000);
}
