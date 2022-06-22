// 建立連線
let provider = "HTTP://127.0.0.1:8545";
web3 = new Web3(new Web3.providers.HttpProvider(provider));

let ca = "0x61933171E708C8bA3bc613ac1De432F7C096269b" //合約地址

let contract;
contract = new web3.eth.Contract(abi, ca); 

var walletAddress;

function getwalletAccount(){
    web3.eth.getAccounts(function(err, addresses){
        if (err){
            alert("找不到帳號地址!");
        }else{
            console.log(addresses)
            for (i in addresses){
                if(document.getElementById("address").value == addresses[i]){
                    walletAddress = document.getElementById("address").value
                    alert("已抓取錢包地址");
                    break
                }else{

                }
            }
        }
    })
}


function login(){
    let addressId = document.getElementById("address").value
    let account = document.getElementById("account").value
    let passWord = document.getElementById("password").value
    if(addressId == "" || account == "" || passWord == ""){
        alert("錢包地址或帳號密碼未輸入!")
    }else{
        contract.methods.getAccount(addressId, account, passWord)
        .call()
        .then(function(data){
            console.log(data)
            if(data == false){
                alert("錢包地址或帳號密碼錯誤!")
            } else if(data == true){
                window.location.href = 'http://61.30.143.169:8000/'
                alert("登入成功")
            }
        })
        .catch(function(error){
            console.log(error)
        })
    }
}

// 創建隨機亂數驗證碼
function getRandom(){
    
    num = Math.floor(Math.random()*100000)
    return num
}
randomData = getRandom()
console.log(randomData)

function forget(){
    
    let addressId = document.getElementById("address").value
    let accountName = document.getElementById("account").value
    let verificatoin = document.getElementById("verificatoin").value
    if (account == "" || verificatoin ==""){
        alert("錢包地址、帳號或驗證碼未輸入!")
    }else{
        contract.methods.getPassword(addressId, accountName)
        .call()
        .then(function(data){
            if (document.getElementById("verificatoin").value == randomData){
                console.log(data)
                alert("PassWord:" + data[1])
            }else{
                alert("verificatoin code is not match")
            }
            
        })
        .catch(function(error){
            console.log(error)
            alert("錢包地址與帳號名稱不匹配")   
        })
    }
}

// 使用 elasticemail 官網的api 不支援 'smtp.gmail.com'
// https://app.elasticemail.com/api/settings/manage-smtp

// Email.send({
//     SecureToken : "74f4a57c-7acb-4b73-a613-2c8e2649cade",
//     To : 'weihe7813@gmail.com',
//     From : "wei4gmaing@gmail.com",
//     Subject : "Random Nunber",
//     Body : randomData,
//     }).then(
//     message => alert(message)
// );

// 透過 Websockets 傳送 userInfo 到 python server
const websocket = new WebSocket("ws://localhost:5268/"); 

websocket.onopen = function () {
    console.log('already bconnet ws');
}

function sendEmail() {
    let mailVal = document.getElementById("Email").value
    let addressId = document.getElementById("address").value
    let accountName = document.getElementById("account").value
    
    const event = {
        walletAddress : addressId,
        accountName : accountName,
        userEmail : mailVal,
        randonNum : randomData,
    }

    websocket.send(JSON.stringify(event));
    alert("查收您的電子郵件")
}


function newAccount(){
    var addressId = document.getElementById("address").value
    var userName = document.getElementById("account").value
    var passWord = document.getElementById("password").value
    var repassWord = document.getElementById("repassWord").value

    if(addressId == "" || account == "" || passWord == "" || repassWord ==""){
        alert("輸入欄位輸入")
    }else if(passWord != repassWord){
        alert("密碼不一致")
    }else{

        // contract.methods.setAccount(addressId, userName, passWord).estimateGas()
        // .send({
        //     from : addressId,
        // })
        // .then(function(data){
        //     alert(data)
        // })
        // .catch(function(error){
        //     console.log(error) 
        //     alert(error) 
        // })

        const gasValue = contract.methods.setAccount(addressId, userName, passWord).estimateGas()
        console.log(gasValue)
        contract.methods.setAccount(addressId, userName, passWord)
        .send({
            from : addressId,
            gas : 110000,
            gasPrice: "3000000",
        })
        .then(function(data){
            alert("註冊成功")
        })
        .catch(function(error){
            console.log(error) 
            alert(error) 
        })
    }
}