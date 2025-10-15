<<<<<<< HEAD
import React, { useState } from 'react';
import { Shield, Users, Lock, TrendingUp, CheckCircle, AlertCircle, Clock, DollarSign, MessageSquare, ArrowRight, FileText, Star, Search, Filter, X, Send, Copy, Check } from 'lucide-react';

const TrustPeer = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [selectedTrade, setSelectedTrade] = useState(null);
  const [selectedCrypto, setSelectedCrypto] = useState('STX');
  const [stxBalance] = useState(1250.50);
  const [tradeDetails, setTradeDetails] = useState({ 
    amount: '', 
    paymentMethod: '',
    transactionId: ''
  });
  const [tradeStep, setTradeStep] = useState('details'); // details, payment, confirm, success
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);
  const [myTradesList, setMyTradesList] = useState([]);
  const [chatMessages, setChatMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [copiedId, setCopiedId] = useState(false);

  // Cryptocurrency options
  const cryptoOptions = [
    { symbol: 'STX', name: 'Stacks', price: 0.52, icon: '🔷' },
    { symbol: 'BTC', name: 'Bitcoin', price: 43250.00, icon: '₿' },
    { symbol: 'ETH', name: 'Ethereum', price: 2280.50, icon: 'Ξ' },
    { symbol: 'USDT', name: 'Tether', price: 1.00, icon: '₮' },
    { symbol: 'BNB', name: 'BNB', price: 312.40, icon: '🔶' },
    { symbol: 'SOL', name: 'Solana', price: 98.75, icon: '◎' }
  ];

  // Sample trade listings
  const tradeListings = [
    {
      id: 1,
      seller: "CryptoKing",
      rating: 4.8,
      trades: 156,
      crypto: "STX",
      amount: "500",
      price: "$0.52",
      paymentMethods: ["Bank Transfer", "PayPal", "Wise"],
      limits: "Min: $50 | Max: $1000",
      responseTime: "~5 mins",
      badge: "Verified",
      status: "online",
      bankDetails: {
        bankName: "Chase Bank",
        accountName: "John Doe",
        accountNumber: "****1234"
      }
    },
    {
      id: 2,
      seller: "BlockchainBob",
      rating: 4.9,
      trades: 243,
      crypto: "BTC",
      amount: "0.05",
      price: "$43,250",
      paymentMethods: ["Bank Transfer", "Zelle"],
      limits: "Min: $100 | Max: $5000",
      responseTime: "~3 mins",
      badge: "Elite",
      status: "online",
      bankDetails: {
        bankName: "Bank of America",
        accountName: "Bob Smith",
        accountNumber: "****5678"
      }
    },
    {
      id: 3,
      seller: "SafeTrader",
      rating: 4.7,
      trades: 89,
      crypto: "ETH",
      amount: "2.5",
      price: "$2,280",
      paymentMethods: ["Cash App", "Venmo"],
      limits: "Min: $500 | Max: $10000",
      responseTime: "~10 mins",
      badge: "Verified",
      status: "away",
      bankDetails: {
        bankName: "Wells Fargo",
        accountName: "Sarah Johnson",
        accountNumber: "****9012"
      }
    },
    {
      id: 4,
      seller: "USDTTrader",
      rating: 4.9,
      trades: 312,
      crypto: "USDT",
      amount: "10000",
      price: "$1.00",
      paymentMethods: ["Bank Transfer", "PayPal", "Wise"],
      limits: "Min: $100 | Max: $20000",
      responseTime: "~2 mins",
      badge: "Elite",
      status: "online",
      bankDetails: {
        bankName: "Citibank",
        accountName: "Mike Wilson",
        accountNumber: "****3456"
      }
    },
    {
      id: 5,
      seller: "SolanaMax",
      rating: 4.6,
      trades: 127,
      crypto: "SOL",
      amount: "50",
      price: "$98.75",
      paymentMethods: ["Zelle", "Cash App"],
      limits: "Min: $200 | Max: $5000",
      responseTime: "~7 mins",
      badge: "Verified",
      status: "online",
      bankDetails: {
        bankName: "TD Bank",
        accountName: "Max Rodriguez",
        accountNumber: "****7890"
      }
    },
    {
      id: 6,
      seller: "BNBMaster",
      rating: 4.8,
      trades: 198,
      crypto: "BNB",
      amount: "15",
      price: "$312.40",
      paymentMethods: ["Bank Transfer", "Wise"],
      limits: "Min: $300 | Max: $8000",
      responseTime: "~4 mins",
      badge: "Elite",
      status: "online",
      bankDetails: {
        bankName: "PNC Bank",
        accountName: "Alex Chen",
        accountNumber: "****2345"
      }
    }
  ];

  const handleStartTrade = (trade) => {
    setSelectedTrade(trade);
    setTradeStep('details');
    setTradeDetails({ amount: '', paymentMethod: '', transactionId: '' });
    setChatMessages([
      { sender: 'system', text: `Connected with ${trade.seller}. Please be polite and professional.`, time: 'Now' }
    ]);
  };

  const handleCreateEscrow = () => {
    if (!tradeDetails.amount || !tradeDetails.paymentMethod) {
      alert('Please fill in all required fields');
      return;
    }
    setTradeStep('payment');
  };

  const handleConfirmPayment = () => {
    if (!tradeDetails.transactionId) {
      alert('Please enter your transaction ID');
      return;
    }
    setTradeStep('confirm');
  };

  const handleCompletePayment = () => {
    const cryptoInfo = cryptoOptions.find(c => c.symbol === selectedTrade.crypto);
    const newTrade = {
      id: Date.now(),
      type: "buy",
      counterparty: selectedTrade.seller,
      crypto: selectedTrade.crypto,
      amount: tradeDetails.amount,
      total: `$${(parseFloat(tradeDetails.amount) * cryptoInfo.price * 1.005).toFixed(2)}`,
      status: "completed",
      stage: "released",
      createdAt: "Just now",
      escrowId: `ESC-${Math.random().toString(36).substr(2, 9).toUpperCase()}`
    };
    
    setMyTradesList([newTrade, ...myTradesList]);
    setShowSuccessMessage(true);
    
    setTimeout(() => {
      setShowSuccessMessage(false);
      setSelectedTrade(null);
      setTradeStep('details');
      setActiveTab('trades');
    }, 3000);
  };

  const handleSendMessage = () => {
    if (!newMessage.trim()) return;
    setChatMessages([...chatMessages, { 
      sender: 'you', 
      text: newMessage, 
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }]);
    setNewMessage('');
    
    // Simulate seller response
    setTimeout(() => {
      setChatMessages(prev => [...prev, {
        sender: selectedTrade.seller,
        text: "I've received your message. Please proceed with the payment.",
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }]);
    }, 2000);
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopiedId(true);
    setTimeout(() => setCopiedId(false), 2000);
  };

  const Dashboard = () => (
    <div className="space-y-6">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-8 rounded-xl shadow-lg">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold mb-2">Welcome to TrustPeer</h1>
            <p className="text-purple-100 mb-4">Trade crypto safely with escrow smart contracts on Stacks</p>
            <div className="flex items-center gap-4">
              <div className="bg-white bg-opacity-20 px-4 py-2 rounded-lg">
                <p className="text-sm text-purple-100">Your Balance</p>
                <p className="text-2xl font-bold">{stxBalance.toFixed(2)} STX</p>
              </div>
              <div className="bg-white bg-opacity-20 px-4 py-2 rounded-lg">
                <p className="text-sm text-purple-100">Total Trades</p>
                <p className="text-2xl font-bold">{myTradesList.length}</p>
              </div>
            </div>
          </div>
          <Shield className="w-24 h-24 text-purple-200" />
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
          <div className="flex items-center justify-between mb-4">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
              <CheckCircle className="w-6 h-6 text-green-600" />
            </div>
            <span className="text-green-600 font-semibold text-sm">+12%</span>
          </div>
          <h3 className="text-gray-600 text-sm">Completed Trades</h3>
          <p className="text-2xl font-bold text-gray-800">{myTradesList.filter(t => t.status === 'completed').length}</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
          <div className="flex items-center justify-between mb-4">
            <div className="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
              <Clock className="w-6 h-6 text-yellow-600" />
            </div>
            <span className="text-yellow-600 font-semibold text-sm">Active</span>
          </div>
          <h3 className="text-gray-600 text-sm">Pending Trades</h3>
          <p className="text-2xl font-bold text-gray-800">{myTradesList.filter(t => t.status === 'in_escrow').length}</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
          <div className="flex items-center justify-between mb-4">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
              <Star className="w-6 h-6 text-purple-600" />
            </div>
            <span className="text-purple-600 font-semibold text-sm">★ 4.9</span>
          </div>
          <h3 className="text-gray-600 text-sm">Your Rating</h3>
          <p className="text-2xl font-bold text-gray-800">Excellent</p>
        </div>
      </div>

      {/* How It Works */}
      <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
        <h2 className="text-xl font-bold text-gray-800 mb-6">How TrustPeer Escrow Works</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="text-center">
            <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-3">
              <Users className="w-8 h-8 text-blue-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">1. Find Trade</h3>
            <p className="text-sm text-gray-600">Browse verified traders and select the best offer</p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-3">
              <Lock className="w-8 h-8 text-purple-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">2. Funds Locked</h3>
            <p className="text-sm text-gray-600">Crypto automatically locked in escrow smart contract</p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-3">
              <DollarSign className="w-8 h-8 text-green-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">3. Make Payment</h3>
            <p className="text-sm text-gray-600">Send fiat payment via agreed method</p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-3">
              <CheckCircle className="w-8 h-8 text-yellow-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">4. Get Crypto</h3>
            <p className="text-sm text-gray-600">Escrow releases crypto to your wallet</p>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <button
          onClick={() => setActiveTab('marketplace')}
          className="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-all"
        >
          <div className="flex items-center justify-between">
            <div className="text-left">
              <h3 className="text-xl font-bold mb-2">Start Trading</h3>
              <p className="text-purple-100">Browse marketplace and find the best deals</p>
            </div>
            <ArrowRight className="w-8 h-8" />
          </div>
        </button>

        <button
          onClick={() => setActiveTab('trades')}
          className="bg-white border-2 border-purple-600 text-purple-600 p-6 rounded-xl shadow-md hover:shadow-lg transition-all"
        >
          <div className="flex items-center justify-between">
            <div className="text-left">
              <h3 className="text-xl font-bold mb-2">View My Trades</h3>
              <p className="text-purple-500">Check your active and completed transactions</p>
            </div>
            <FileText className="w-8 h-8" />
          </div>
        </button>
      </div>
    </div>
  );

  const Marketplace = () => (
    <div className="space-y-6">
      {/* Crypto Selector */}
      <div className="bg-white p-4 rounded-xl shadow-md border border-gray-200">
        <p className="text-sm font-semibold text-gray-700 mb-3">Select Cryptocurrency</p>
        <div className="grid grid-cols-2 md:grid-cols-6 gap-3">
          {cryptoOptions.map((crypto) => (
            <button
              key={crypto.symbol}
              onClick={() => setSelectedCrypto(crypto.symbol)}
              className={`p-3 rounded-lg border-2 transition-all ${
                selectedCrypto === crypto.symbol
                  ? 'border-purple-600 bg-purple-50'
                  : 'border-gray-200 hover:border-gray-300'
              }`}
            >
              <div className="text-2xl mb-1">{crypto.icon}</div>
              <p className="font-bold text-sm">{crypto.symbol}</p>
              <p className="text-xs text-gray-600">${crypto.price < 10 ? crypto.price.toFixed(2) : crypto.price.toLocaleString()}</p>
            </button>
          ))}
        </div>
      </div>

      {/* Search and Filters */}
      <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
        <div className="flex flex-col md:flex-row gap-4">
          <div className="flex-1 relative">
            <Search className="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
            <input
              type="text"
              placeholder="Search traders..."
              className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
          </div>
          <select className="px-6 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500">
            <option>Buy Crypto</option>
            <option>Sell Crypto</option>
          </select>
        </div>
      </div>

      {/* Trade Listings */}
      <div className="space-y-4">
        {tradeListings
          .filter(trade => selectedCrypto === 'STX' || trade.crypto === selectedCrypto)
          .map((trade) => {
            const cryptoInfo = cryptoOptions.find(c => c.symbol === trade.crypto);
            return (
              <div key={trade.id} className="bg-white p-6 rounded-xl shadow-md border border-gray-200 hover:shadow-lg transition-shadow">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-4">
                    <div className="w-16 h-16 bg-gradient-to-r from-purple-400 to-blue-400 rounded-full flex items-center justify-center text-white font-bold text-xl">
                      {trade.seller[0]}
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <h3 className="font-bold text-lg">{trade.seller}</h3>
                        <span className={`px-2 py-1 rounded text-xs font-semibold ${
                          trade.badge === 'Elite' ? 'bg-yellow-100 text-yellow-800' : 'bg-blue-100 text-blue-800'
                        }`}>
                          {trade.badge}
                        </span>
                        <div className={`w-2 h-2 rounded-full ${trade.status === 'online' ? 'bg-green-500' : 'bg-gray-400'}`}></div>
                      </div>
                      <div className="flex items-center gap-3 text-sm text-gray-600 mt-1">
                        <div className="flex items-center gap-1">
                          <Star className="w-4 h-4 text-yellow-500 fill-yellow-500" />
                          <span>{trade.rating}</span>
                        </div>
                        <span>•</span>
                        <span>{trade.trades} trades</span>
                        <span>•</span>
                        <span>{trade.responseTime}</span>
                      </div>
                    </div>
                  </div>

                  <div className="text-right">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-2xl">{cryptoInfo?.icon}</span>
                      <span className="text-xl font-bold text-gray-800">{trade.crypto}</span>
                    </div>
                    <p className="text-sm text-gray-600">{trade.price} per coin</p>
                  </div>
                </div>

                <div className="mt-4 grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-gray-200">
                  <div>
                    <p className="text-sm text-gray-600 mb-1">Available</p>
                    <p className="font-semibold text-gray-800">{trade.amount} {trade.crypto}</p>
                  </div>
                  <div>
                    <p className="text-sm text-gray-600 mb-1">Limits</p>
                    <p className="font-semibold text-gray-800 text-sm">{trade.limits}</p>
                  </div>
                  <div>
                    <p className="text-sm text-gray-600 mb-1">Payment Methods</p>
                    <div className="flex flex-wrap gap-1">
                      {trade.paymentMethods.map((method, idx) => (
                        <span key={idx} className="px-2 py-1 bg-gray-100 rounded text-xs">
                          {method}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="mt-4 flex gap-3">
                  <button
                    onClick={() => handleStartTrade(trade)}
                    className="flex-1 bg-purple-600 text-white py-3 rounded-lg hover:bg-purple-700 font-semibold flex items-center justify-center gap-2"
                  >
                    Start Trade <ArrowRight className="w-4 h-4" />
                  </button>
                  <button className="px-6 py-3 border border-gray-300 rounded-lg hover:bg-gray-50 flex items-center gap-2">
                    <MessageSquare className="w-4 h-4" />
                    Chat
                  </button>
                </div>
              </div>
            );
          })}
      </div>
    </div>
  );

  const MyTrades = () => (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800">My Trades</h2>
        <select className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500">
          <option>All Trades</option>
          <option>In Progress</option>
          <option>Completed</option>
          <option>Disputed</option>
        </select>
      </div>

      {myTradesList.length === 0 ? (
        <div className="bg-white p-12 rounded-xl shadow-md border border-gray-200 text-center">
          <FileText className="w-16 h-16 text-gray-300 mx-auto mb-4" />
          <h3 className="text-xl font-bold text-gray-800 mb-2">No Trades Yet</h3>
          <p className="text-gray-600 mb-6">Start your first trade in the marketplace</p>
          <button
            onClick={() => setActiveTab('marketplace')}
            className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700 font-semibold"
          >
            Browse Marketplace
          </button>
        </div>
      ) : (
        <div className="space-y-4">
          {myTradesList.map((trade) => (
            <div key={trade.id} className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center ${
                    trade.type === 'buy' ? 'bg-green-100' : 'bg-blue-100'
                  }`}>
                    <TrendingUp className={`w-6 h-6 ${
                      trade.type === 'buy' ? 'text-green-600' : 'text-blue-600'
                    }`} />
                  </div>
                  <div>
                    <p className="font-bold text-gray-800">
                      {trade.type === 'buy' ? 'Bought' : 'Sold'} {trade.amount} {trade.crypto}
                    </p>
                    <p className="text-sm text-gray-600">
                      {trade.type === 'buy' ? 'From' : 'To'}: {trade.counterparty}
                    </p>
                  </div>
                </div>

                <div className="text-right">
                  <p className="font-bold text-gray-800">{trade.total}</p>
                  <span className={`inline-block px-3 py-1 rounded-full text-xs font-semibold mt-1 ${
                    trade.status === 'completed' ? 'bg-green-100 text-green-800' :
                    trade.status === 'in_escrow' ? 'bg-yellow-100 text-yellow-800' :
                    'bg-red-100 text-red-800'
                  }`}>
                    {trade.status === 'in_escrow' ? 'In Escrow' :
                     trade.status === 'completed' ? 'Completed' : 'Disputed'}
                  </span>
                </div>
              </div>

              <div className="bg-gray-50 p-4 rounded-lg mb-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <span className="text-sm text-gray-600">Escrow ID:</span>
                    <p className="text-sm font-mono font-semibold">{trade.escrowId}</p>
                  </div>
                  <div>
                    <span className="text-sm text-gray-600">Created:</span>
                    <p className="text-sm font-semibold">{trade.createdAt}</p>
                  </div>
                </div>
              </div>

              {trade.status === 'completed' && (
                <div className="flex items-center justify-center gap-2 text-green-600 bg-green-50 py-3 rounded-lg">
                  <CheckCircle className="w-5 h-5" />
                  <span className="font-semibold">Trade Completed Successfully</span>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );

  const TradeModal = () => {
    if (!selectedTrade) return null;

    const cryptoInfo = cryptoOptions.find(c => c.symbol === selectedTrade.crypto);
    const calculatedPrice = tradeDetails.amount ? (parseFloat(tradeDetails.amount) * cryptoInfo.price).toFixed(2) : '0.00';
    const escrowFee = tradeDetails.amount ? (parseFloat(tradeDetails.amount) * cryptoInfo.price * 0.005).toFixed(2) : '0.00';
    const totalPayment = tradeDetails.amount ? (parseFloat(calculatedPrice) * 1.005).toFixed(2) : '0.00';

    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
        <div className="bg-white rounded-xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
          {showSuccessMessage && (
            <div className="bg-green-50 border-b-2 border-green-200 p-6 text-center">
              <CheckCircle className="w-16 h-16 text-green-600 mx-auto mb-3" />
              <h3 className="text-2xl font-bold text-green-800 mb-2">Payment Successful!</h3>
              <p className="text-green-700">Your crypto will be released from escrow shortly</p>
            </div>
          )}

          {!showSuccessMessage && (
            <>
              <div className="p-6 border-b border-gray-200">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <h2 className="text-2xl font-bold text-gray-800">Trade with {selectedTrade.seller}</h2>
                    <div className="flex items-center gap-2 bg-purple-100 px-3 py-1 rounded-lg">
                      <span className="text-2xl">{cryptoInfo?.icon}</span>
                      <span className="font-bold text-purple-700">{selectedTrade.crypto}</span>
                    </div>
                  </div>
                  <button
                    onClick={() => {
                      setSelectedTrade(null);
                      setTradeStep('details');
                    }}
                    className="text-gray-500 hover:text-gray-700"
                  >
                    <X className="w-6 h-6" />
                  </button>
                </div>

                {/* Progress Steps */}
                <div className="flex items-center justify-between mt-6">
                  <div className="flex items-center gap-2">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                      tradeStep === 'details' ? 'bg-purple-600 text-white' : 'bg-gray-300 text-gray-600'
                    }`}>
                      1
                    </div>
                    <span className="text-sm font-semibold">Details</span>
                  </div>
                  <div className="flex-1 h-1 bg-gray-300 mx-2"></div>
                  <div className="flex items-center gap-2">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                      tradeStep === 'payment' || tradeStep === 'confirm' || tradeStep === 'success' ? 'bg-purple-600 text-white' : 'bg-gray-300 text-gray-600'
                    }`}>
                      2
                    </div>
                    <span className="text-sm font-semibold">Payment</span>
                  </div>
                  <div className="flex-1 h-1 bg-gray-300 mx-2"></div>
                  <div className="flex items-center gap-2">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                      tradeStep === 'confirm' || tradeStep === 'success' ? 'bg-purple-600 text-white' : 'bg-gray-300 text-gray-600'
                    }`}>
                      3
                    </div>
                    <span className="text-sm font-semibold">Confirm</span>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 p-6">
                {/* Main Content */}
                <div className="md:col-span-2 space-y-6">
                  {/* Step 1: Trade Details */}
                  {tradeStep === 'details' && (
                    <>
                      <div className="bg-purple-50 border border-purple-200 p-4 rounded-lg">
                        <div className="flex items-center gap-3">
                          <div className="w-12 h-12 bg-gradient-to-r from-purple-400 to-blue-400 rounded-full flex items-center justify-center text-white font-bold">
                            {selectedTrade.seller[0]}
                          </div>
                          <div>
                            <p className="font-bold text-gray-800">{selectedTrade.seller}</p>
                            <div className="flex items-center gap-2 text-sm">
                              <Star className="w-4 h-4 text-yellow-500 fill-yellow-500" />
                              <span>{selectedTrade.rating}</span>
                              <span className="text-gray-600">• {selectedTrade.trades} trades</span>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-2">
                          Amount to buy
                        </label>
                        <div className="flex gap-2">
                          <input
                            type="number"
                            placeholder="Enter amount"
                            value={tradeDetails.amount}
                            onChange={(e) => setTradeDetails({...tradeDetails, amount: e.target.value})}
                            className="flex-1 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                          />
                          <div className="w-32 bg-gray-100 rounded-lg flex items-center justify-center font-semibold">
                            {selectedTrade.crypto}
                          </div>
                        </div>
                        <p className="text-xs text-gray-600 mt-1">
                          Available: {selectedTrade.amount} {selectedTrade.crypto}
                        </p>
                      </div>

                      <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-2">
                          You will pay
                        </label>
                        <div className="p-4 bg-gray-50 rounded-lg border border-gray-300">
                          <p className="text-3xl font-bold text-gray-800">${calculatedPrice}</p>
                          <p className="text-sm text-gray-600 mt-1">USD (including 0.5% escrow fee)</p>
                        </div>
                      </div>

                      <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-2">
                          Payment Method
                        </label>
                        <select 
                          value={tradeDetails.paymentMethod}
                          onChange={(e) => setTradeDetails({...tradeDetails, paymentMethod: e.target.value})}
                          className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                        >
                          <option value="">Select payment method</option>
                          {selectedTrade.paymentMethods.map((method, idx) => (
                            <option key={idx} value={method}>{method}</option>
                          ))}
                        </select>
                      </div>

                      <div className="bg-blue-50 border border-blue-200 p-4 rounded-lg">
                        <div className="flex items-start gap-3">
                          <Shield className="w-5 h-5 text-blue-600 mt-0.5" />
                          <div>
                            <p className="font-semibold text-blue-900 mb-1">Escrow Protection Active</p>
                            <p className="text-sm text-blue-700">
                              {tradeDetails.amount || '0'} {selectedTrade.crypto} will be locked in our Clarity smart contract and released only after payment confirmation.
                            </p>
                          </div>
                        </div>
                      </div>

                      <button
                        onClick={handleCreateEscrow}
                        disabled={!tradeDetails.amount || !tradeDetails.paymentMethod}
                        className="w-full bg-purple-600 text-white py-4 rounded-lg hover:bg-purple-700 font-semibold disabled:bg-gray-300 disabled:cursor-not-allowed text-lg"
                      >
                        Create Escrow & Continue
                      </button>
                    </>
                  )}

                  {/* Step 2: Payment Instructions */}
                  {tradeStep === 'payment' && (
                    <>
                      <div className="bg-green-50 border border-green-200 p-4 rounded-lg">
                        <div className="flex items-center gap-3 mb-3">
                          <Lock className="w-6 h-6 text-green-600" />
                          <p className="font-bold text-green-800">Escrow Created Successfully!</p>
                        </div>
                        <p className="text-sm text-green-700">
                          {tradeDetails.amount} {selectedTrade.crypto} is now locked in escrow. Complete your payment to release the funds.
                        </p>
                      </div>

                      <div className="bg-white border-2 border-purple-600 p-6 rounded-lg">
                        <h3 className="text-lg font-bold text-gray-800 mb-4">Payment Instructions</h3>
                        
                        <div className="space-y-4">
                          <div>
                            <p className="text-sm text-gray-600 mb-1">Payment Method</p>
                            <p className="font-semibold text-gray-800 text-lg">{tradeDetails.paymentMethod}</p>
                          </div>

                          <div className="border-t pt-4">
                            <p className="text-sm text-gray-600 mb-3">Send payment to:</p>
                            
                            <div className="bg-gray-50 p-4 rounded-lg space-y-3">
                              <div className="flex justify-between items-center">
                                <div>
                                  <p className="text-xs text-gray-600">Bank Name</p>
                                  <p className="font-semibold">{selectedTrade.bankDetails.bankName}</p>
                                </div>
                                <button
                                  onClick={() => copyToClipboard(selectedTrade.bankDetails.bankName)}
                                  className="p-2 hover:bg-gray-200 rounded"
                                >
                                  {copiedId ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
                                </button>
                              </div>

                              <div className="flex justify-between items-center">
                                <div>
                                  <p className="text-xs text-gray-600">Account Name</p>
                                  <p className="font-semibold">{selectedTrade.bankDetails.accountName}</p>
                                </div>
                                <button
                                  onClick={() => copyToClipboard(selectedTrade.bankDetails.accountName)}
                                  className="p-2 hover:bg-gray-200 rounded"
                                >
                                  {copiedId ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
                                </button>
                              </div>

                              <div className="flex justify-between items-center">
                                <div>
                                  <p className="text-xs text-gray-600">Account Number</p>
                                  <p className="font-semibold">{selectedTrade.bankDetails.accountNumber}</p>
                                </div>
                                <button
                                  onClick={() => copyToClipboard(selectedTrade.bankDetails.accountNumber)}
                                  className="p-2 hover:bg-gray-200 rounded"
                                >
                                  {copiedId ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
                                </button>
                              </div>

                              <div className="border-t pt-3 mt-3">
                                <p className="text-xs text-gray-600">Amount to Send</p>
                                <p className="text-2xl font-bold text-purple-600">${totalPayment}</p>
                              </div>
                            </div>
                          </div>

                          <div className="bg-yellow-50 border border-yellow-200 p-3 rounded-lg">
                            <p className="text-sm text-yellow-800">
                              <strong>Important:</strong> Make sure to send exactly ${totalPayment} and note your transaction ID.
                            </p>
                          </div>
                        </div>
                      </div>

                      <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-2">
                          Enter Transaction/Reference ID
                        </label>
                        <input
                          type="text"
                          placeholder="e.g., TXN123456789"
                          value={tradeDetails.transactionId}
                          onChange={(e) => setTradeDetails({...tradeDetails, transactionId: e.target.value})}
                          className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                        />
                        <p className="text-xs text-gray-600 mt-1">
                          Enter your payment confirmation number or transaction ID
                        </p>
                      </div>

                      <div className="flex gap-3">
                        <button
                          onClick={() => setTradeStep('details')}
                          className="flex-1 border border-gray-300 py-3 rounded-lg hover:bg-gray-50 font-semibold"
                        >
                          Back
                        </button>
                        <button
                          onClick={handleConfirmPayment}
                          disabled={!tradeDetails.transactionId}
                          className="flex-1 bg-purple-600 text-white py-3 rounded-lg hover:bg-purple-700 font-semibold disabled:bg-gray-300 disabled:cursor-not-allowed"
                        >
                          I've Made Payment
                        </button>
                      </div>
                    </>
                  )}

                  {/* Step 3: Confirm Payment */}
                  {tradeStep === 'confirm' && (
                    <>
                      <div className="bg-blue-50 border border-blue-200 p-6 rounded-lg text-center">
                        <Clock className="w-16 h-16 text-blue-600 mx-auto mb-3" />
                        <h3 className="text-xl font-bold text-gray-800 mb-2">Verify Your Payment</h3>
                        <p className="text-gray-600">
                          Please review your payment details before confirming
                        </p>
                      </div>

                      <div className="bg-white border border-gray-300 p-6 rounded-lg space-y-4">
                        <div className="flex justify-between pb-3 border-b">
                          <span className="text-gray-600">Cryptocurrency</span>
                          <span className="font-semibold">{tradeDetails.amount} {selectedTrade.crypto}</span>
                        </div>
                        <div className="flex justify-between pb-3 border-b">
                          <span className="text-gray-600">Amount Paid</span>
                          <span className="font-semibold">${totalPayment}</span>
                        </div>
                        <div className="flex justify-between pb-3 border-b">
                          <span className="text-gray-600">Payment Method</span>
                          <span className="font-semibold">{tradeDetails.paymentMethod}</span>
                        </div>
                        <div className="flex justify-between pb-3 border-b">
                          <span className="text-gray-600">Transaction ID</span>
                          <span className="font-semibold font-mono">{tradeDetails.transactionId}</span>
                        </div>
                        <div className="flex justify-between pb-3 border-b">
                          <span className="text-gray-600">Seller</span>
                          <span className="font-semibold">{selectedTrade.seller}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-gray-600">Escrow Fee</span>
                          <span className="font-semibold">${escrowFee}</span>
                        </div>
                      </div>

                      <div className="bg-yellow-50 border border-yellow-200 p-4 rounded-lg">
                        <div className="flex items-start gap-3">
                          <AlertCircle className="w-5 h-5 text-yellow-600 mt-0.5" />
                          <div>
                            <p className="font-semibold text-yellow-900 mb-1">Important Notice</p>
                            <p className="text-sm text-yellow-800">
                              By confirming, you declare that you have completed the payment. The seller will verify and release the crypto from escrow.
                            </p>
                          </div>
                        </div>
                      </div>

                      <div className="flex gap-3">
                        <button
                          onClick={() => setTradeStep('payment')}
                          className="flex-1 border border-gray-300 py-3 rounded-lg hover:bg-gray-50 font-semibold"
                        >
                          Back
                        </button>
                        <button
                          onClick={handleCompletePayment}
                          className="flex-1 bg-green-600 text-white py-4 rounded-lg hover:bg-green-700 font-semibold text-lg flex items-center justify-center gap-2"
                        >
                          <CheckCircle className="w-5 h-5" />
                          Confirm Payment
                        </button>
                      </div>
                    </>
                  )}
                </div>

                {/* Chat Sidebar */}
                <div className="bg-gray-50 rounded-lg border border-gray-300 flex flex-col h-[600px]">
                  <div className="p-4 border-b border-gray-300 bg-white rounded-t-lg">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-gradient-to-r from-purple-400 to-blue-400 rounded-full flex items-center justify-center text-white font-bold">
                        {selectedTrade.seller[0]}
                      </div>
                      <div>
                        <p className="font-semibold text-gray-800">{selectedTrade.seller}</p>
                        <div className="flex items-center gap-1">
                          <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                          <span className="text-xs text-gray-600">Online</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="flex-1 overflow-y-auto p-4 space-y-3">
                    {chatMessages.map((msg, idx) => (
                      <div key={idx} className={`flex ${msg.sender === 'you' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`max-w-[80%] ${
                          msg.sender === 'system' ? 'w-full' : ''
                        }`}>
                          {msg.sender === 'system' ? (
                            <div className="bg-blue-50 border border-blue-200 p-2 rounded-lg text-center">
                              <p className="text-xs text-blue-700">{msg.text}</p>
                            </div>
                          ) : (
                            <>
                              <div className={`p-3 rounded-lg ${
                                msg.sender === 'you' 
                                  ? 'bg-purple-600 text-white rounded-br-none' 
                                  : 'bg-white border border-gray-300 rounded-bl-none'
                              }`}>
                                <p className="text-sm">{msg.text}</p>
                              </div>
                              <p className="text-xs text-gray-500 mt-1 px-1">{msg.time}</p>
                            </>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>

                  <div className="p-4 border-t border-gray-300 bg-white rounded-b-lg">
                    <div className="flex gap-2">
                      <input
                        type="text"
                        placeholder="Type a message..."
                        value={newMessage}
                        onChange={(e) => setNewMessage(e.target.value)}
                        onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                        className="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                      />
                      <button
                        onClick={handleSendMessage}
                        disabled={!newMessage.trim()}
                        className="bg-purple-600 text-white p-2 rounded-lg hover:bg-purple-700 disabled:bg-gray-300"
                      >
                        <Send className="w-5 h-5" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-40">
        <div className="px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg flex items-center justify-center">
                <Shield className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-800">TrustPeer</h1>
                <p className="text-xs text-gray-600">P2P Trading on Stacks</p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="hidden md:flex items-center gap-2 bg-purple-50 px-4 py-2 rounded-lg">
                <Lock className="w-4 h-4 text-purple-600" />
                <span className="text-sm font-semibold text-purple-700">Wallet Connected</span>
              </div>
              <div className="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center">
                <Users className="w-5 h-5 text-gray-600" />
              </div>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <nav className="px-6 border-t border-gray-200">
          <div className="flex space-x-8">
            {[
              { id: 'dashboard', label: 'Dashboard', icon: TrendingUp },
              { id: 'marketplace', label: 'Marketplace', icon: Users },
              { id: 'trades', label: 'My Trades', icon: FileText }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-2 py-4 border-b-2 transition-colors ${
                  activeTab === tab.id
                    ? 'border-purple-600 text-purple-600'
                    : 'border-transparent text-gray-600 hover:text-gray-800'
                }`}
              >
                <tab.icon className="w-5 h-5" />
                {tab.label}
              </button>
            ))}
          </div>
        </nav>
      </header>

      {/* Main Content */}
      <main className="p-6 max-w-7xl mx-auto">
        {activeTab === 'dashboard' && <Dashboard />}
        {activeTab === 'marketplace' && <Marketplace />}
        {activeTab === 'trades' && <MyTrades />}
      </main>

      {/* Trade Modal */}
      <TradeModal />

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 px-6 py-4 mt-12">
        <div className="max-w-7xl mx-auto flex items-center justify-between text-sm text-gray-600">
          <p>© 2025 TrustPeer. Built on Stacks Blockchain with Clarity Smart Contracts</p>
          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1">
              <Shield className="w-4 h-4" />
              Secured by Escrow
            </span>
            <span>•</span>
            <span>0.5% Platform Fee</span>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default TrustPeer;
=======

>>>>>>> 44c109abecee7f8c697888d1913d149f26f312bb
