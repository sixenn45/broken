const { spawn } = require('child_process');

module.exports = async (req, res) => {
  console.log('🔄 Starting Telegram UserBot...');
  
  // Check if environment variables are set
  if (!process.env.API_ID || !process.env.API_HASH || !process.env.PHONE_NUMBER) {
    return res.status(500).json({
      status: 'error',
      message: 'Environment variables not set! Please setup API_ID, API_HASH, and PHONE_NUMBER in Vercel dashboard.',
      timestamp: new Date().toISOString()
    });
  }
  
  try {
    // Jalankan bot
    const pythonProcess = spawn('python', ['bot.py'], {
      detached: true,
      stdio: 'ignore'
    });
    
    pythonProcess.unref();
    
    res.status(200).json({
      status: 'success',
      message: 'Bot started!',
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    res.status(500).json({
      status: 'error',
      message: error.message
    });
