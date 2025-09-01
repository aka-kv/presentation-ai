# AI Voice Presentation - Enhanced Interactive Demo

This is a **fully functional prototype** of an AI voice presentation system with advanced slide navigation and logging capabilities. Built for technical demonstration using Flask + WebRTC + OpenAI Realtime API with function calling.

## 🎯 Key Features Implemented

✅ **Interactive Slide Navigation**: AI can navigate slides via voice commands ("next slide", "go to slide 2")  
✅ **Real-time Voice Interruptions**: Speak anytime to interrupt and ask questions  
✅ **Smart Slide Awareness**: AI knows which slide is currently displayed  
✅ **Comprehensive Logging**: All interactions logged with timestamps at `/logs`  
✅ **Minimalistic UI**: Clean, modern interface with custom color scheme  
✅ **Function Calling**: OpenAI functions for slide navigation and awareness  

## 🛠️ Technical Stack

- **Backend**: Flask (Python) with logging endpoints and session management
- **Frontend**: Vanilla HTML/JS with WebRTC for real-time audio
- **AI Integration**: OpenAI Realtime API with custom function definitions
- **Navigation**: JavaScript-based slide management with AI integration
- **Logging**: Real-time event tracking and display system

## 📦 Quick Setup

1. **Install dependencies:**
   ```powershell
   pip install Flask httpx python-dotenv
   ```

2. **Your API key is already set up in `.env` file** ✅

3. **Run the app:**
   ```powershell
   python app.py
   ```

4. **Open Chrome with microphone permissions:**
   ```powershell
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --unsafely-treat-insecure-origin-as-secure="http://localhost:8116" --user-data-dir=%TEMP%\chrome_dev
   ```

5. **Navigate to:** `http://localhost:8116`

## 🎭 Demo Flow & Advanced Features

### Core Presentation Flow
1. **Auto-connection**: App connects to OpenAI when page loads
2. **Start Presentation**: Click "Start Presentation" - AI begins presenting current slide
3. **Smart Navigation**: AI automatically navigates slides when you say:
   - *"Next slide"* or *"Go to slide 2"*
   - *"Previous slide"* or *"Go back"*
   - *"Show me the Mars slide"*

### Voice Interaction Testing
4. **Test Interruptions**: Try these while AI is speaking:
   - *"Wait, can you explain that again?"*
   - *"What's the largest planet?"*  
   - *"Tell me more about Mars' moons"*
   - *"Skip to the next slide"*
   - *"How big is the Sun compared to Earth?"*

### Advanced Features
5. **Manual Navigation**: Use Previous/Next buttons alongside voice commands
6. **Live Logging**: Visit `/logs` to see all interactions in real-time
7. **Slide Awareness**: AI always knows which slide is currently displayed
8. **Natural Flow**: AI stops, answers questions, navigates slides, then continues

## 🏆 Advanced Technical Demonstrations

- **OpenAI Function Calling**: AI uses custom functions to navigate slides programmatically
- **Real-time WebRTC**: Direct browser-to-OpenAI audio connection with data channels
- **Smart Slide Management**: AI tracks current slide and navigates based on voice commands
- **Comprehensive Logging**: All events (connections, slides, AI messages) logged with timestamps
- **Interruption Handling**: AI immediately responds when user speaks
- **Context Awareness**: AI remembers slide content and current position
- **Minimalistic UI**: Clean interface with custom color scheme (Blue/Purple gradient)
- **Audio Visualization**: Live feedback showing user (blue) vs AI (purple) audio

1. **Grant microphone permissions** when prompted
2. **Wait for "Connected"** status (should connect automatically)
3. **Click "Start Narration"** to begin the presentation
4. **Listen to the AI** narrate Slide 1 (Solar System), then Slide 2 (Mars)
5. **Interrupt anytime** by speaking - the AI will stop and respond to your questions
6. **Ask questions** like:
   - "Can you explain that again?"
   - "Tell me more about Mars' moons"
   - "What's the largest planet?"
   - "Skip to the next slide"

## 🏗️ Enhanced Architecture

- **Backend**: Flask server with multiple endpoints:
  - `/` - Main presentation interface
  - `/session` - OpenAI ephemeral key generation
  - `/logs` - Real-time logging dashboard
  - `/api/log` - Event logging API
  - `/api/slide/<number>` - Slide tracking API
- **Frontend**: Enhanced HTML/JS with:
  - WebRTC for real-time audio communication
  - JavaScript slide management with smooth transitions
  - Real-time logging to backend
  - Custom UI with modern gradient design
- **AI Integration**: 
  - Direct WebRTC connection to OpenAI Realtime API
  - Custom function definitions for slide navigation
  - Slide awareness and context management
- **Audio Processing**: Web Audio API for live visualizations with custom colors

## 🔧 Customization Options

- **Add More Slides**: 
  - Edit slide content in `templates/index.html` 
  - Update `totalSlides` variable in JavaScript
  - Add slide data to `getSlideContent()` function
- **Change AI Voice**: Update the "voice" parameter in `app.py` (options: alloy, echo, fable, onyx, nova, shimmer)
- **Modify AI Instructions**: Edit the instructions in the `startNarration()` function
- **Custom Color Scheme**: Update CSS variables for different color themes
- **Add New Functions**: Define additional OpenAI functions for more AI capabilities
- **Enhanced Logging**: Modify logging events in JavaScript and Flask endpoints

## 🐛 Troubleshooting

- **"OPENAI_API_KEY not set"**: Make sure you've set the environment variable before running the app
- **Microphone not working**: Use the Chrome command with `--unsafely-treat-insecure-origin-as-secure` flag
- **Connection issues**: Check your internet connection and API key validity
- **No audio**: Ensure your browser has microphone permissions and speakers are working

## 📝 Important Notes

- The app runs on **port 8116** by default
- **Chrome is recommended** for development due to WebRTC compatibility
- The AI uses **OpenAI function calling** to navigate slides automatically
- **Real-time logging** tracks all interactions - check `/logs` for detailed activity
- Audio visualizers show user voice (blue) vs AI response (purple)
- **Slide navigation works both ways**: voice commands AND manual buttons
- All events are logged with timestamps for debugging and analysis

## 🎨 UI Color Scheme

The interface uses a modern gradient design with these colors:
- **Primary Blue**: `#013BDB` 
- **Light Blue**: `#33B8FF`
- **Dark Navy**: `#0D1938`
- **Purple Accent**: `#A855F7`
- **White**: Clean backgrounds and text
