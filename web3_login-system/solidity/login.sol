// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0 <0.7.0;

contract login{

    struct Account{
        address accountId;
        string userName;
        uint passWord;
        bool exist;
    }
    
    mapping (string => Account) Accounts;

    //註冊
    function setAccount(address _accountId, string memory _userName, uint _passWord) public {
        require(Accounts[_userName].exist == false, "帳號已存在");
        // require(Accounts[_userName].accountId == _accountId, "帳號已存在");
        Accounts[_userName].accountId = _accountId;
        Accounts[_userName].userName = _userName;
        Accounts[_userName].passWord = _passWord;
        Accounts[_userName].exist = true;    
    }

    //登入驗證
    function getAccount(address _accountId, string memory _userName, uint _passWord) view public returns(bool) {
        if (Accounts[_userName].accountId != _accountId || Accounts[_userName].exist == false || Accounts[_userName].passWord != _passWord ){
            return(false);
        } else if(Accounts[_userName].accountId == _accountId && Accounts[_userName].exist != false && Accounts[_userName].passWord == _passWord){
            return(true);
        }
    }

    // 取得密碼
    function getPassword(address _accountId, string memory _userName) view public returns(string memory,uint){
        require(Accounts[_userName].accountId == _accountId && Accounts[_userName].exist != false, "不匹配");
        return(
            Accounts[_userName].userName,
            Accounts[_userName].passWord
        );
        
    }
    //檢查帳號是否存在
    function checkAccont(string memory _uesrName) view public returns(bool){
        if (Accounts[_uesrName].exist == true){
            return(true);
        }else{
            return(false);
        }
    }
      //登入
    // function getAccount(string memory _userName, uint _passWord) view public returns(string memory) {
    //     if (Accounts[_userName].time == 0){
    //         return("帳號不存在");
    //     } else if(Accounts[_userName].time != 0 && Accounts[_userName].passWord != _passWord){
    //         return("密碼錯誤");
    //     } else if(Accounts[_userName].time != 0 && Accounts[_userName].passWord == _passWord){
    //         return("Login sucessful");
    //     }
    // }

}