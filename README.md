# pcoin
**# Welcome **
This is an academic project in which I implemented core features of a cryptocurrency, based on blockchain technology.

**# Table of Contents**
1. Introduction
2. Getting started
3. Setting up the project
4. Useful resources


**# 1. Introduction**
Blockchain is a distributed database technology in which information is stored in containers,called 'blocks'. Each block is connected to its previous block, thus creating a chain of blocks.Cryptocurrency is just one of the possible use-cases of this technology and serves as a good application to understand the blockchain. The key USP of blockchain is immutability of data once it is mined into a block( it can be changed if more than 51% of the nodes on the network agree to the change). It provides decentralization as it removes a single governing authority and divides the trust to the community.
I developed this project with the help of a course on udemy. It is a great starting project for someone who wants to understand blockchain and get hands-on experience in development with Python.

**# 2. Getting started**
* Terminology 
* **Node :** It is a computer on the blockchain network. A node can have one or more wallets. Each wallet has a unique public-private key set associated with it.
* **Public Key :** A unique string which is used to identify a wallet uniquely on the network. All the transactions are made to and from this address.
* **Private Key :** A unique key, which is provided to each wallet (generated with the public key). It is used to sign the transaction. Transactions are verified using private keys.
* **Block** : It is a unit in which data is stored in a blockchain. It contains : Timestamp, List of transactions that are mined into it, The proof of work number(PoW),hash of the previous block and other information, which can be different for each use-case of the blockchain.
* **Transactions** : Exchange of some entity(in this case, coins) between different nodes on the network. They have to be stored immutably on the ledger.
* **Mining** : The act of adding a block into the blockchain by verifying the transactions and solving a complex mathematical puzzle to produce the PoW. Anyone who does mining is called a **Miner**. Miners are rewarded a certain amount of coins when they successfully mine a block.
* **Open-Transactions** : This is the list of transactions which have not been mined into a block yet.
* **Proof of Work(PoW)** : Mining requires the miner to generate a number, which when combined with other information of the block , should generate a hash value that matches a pre-given pattern(a certain number of leading zeroes,in case of bitcoin). The computational difficulty of generating PoW is increased time to time in order to keep number of coins in the system within a limit. The PoW increases the time required to mine a block, thus making it difficult for the hackers to manipulate the blocks.
* **Blockchain**It is the list of connected blocks. Each block is added on the top of previous blocks.

## Security mechanisms
* **1. Previous hashes** : Each block contains the hash value of previous block. Hash value is generating by using SHA_256 algorithm.
            Changing anything in any block will lead to a different hash-value for that block and it will not match              the hash stored in the next block, hence this will be rejected by the network. However, a hacker may change the has value of manipulated block in the next block..and so on. To prevent this, second security mechanism is added .
* **2. Proof of Work** : Mining a block requires certain amount of computational resources and time. Nodes on the network follow "The longest chain survives" consensus algorithm. By the time a 'bad miner' manipulates a set of blocks, the 'good miners' would have increased the chain length. Hence the unmanipulated chain always survives.
* **3. Public-Private Keys** : The list of open-transactions could be manipulated. To prevent this, each transaction is digitally signed by the sender using his/her private key. 

## Third-Party libraries 
* Hashlib : To generate SHA-256 Hash value for blocks.
* Flask : To design the API using python.
* Cryptography,Pycrytptodome : To generate public-private keys and sign the transactions.
* Json : To format the data.

# Setting up the project
Different nodes on the network are simulated by running the project on different ports.
* **Step 1** : Clone or download the project.
* **Step 2** : Set up a new environment using anaconda-navigator. This allows us to import libraries that are required in this project. Let us name the env variable as 'pycoin'
* **Step 3**: Install following packages in 'pycoin' : Flask , Flask-CORS, pycryptodome, cryptodome.
* **Step 4** : Go to the directory of the project and open the terminal. Activate your environment by following command : _source activate pycoin_ .
* **Step 4** : Run the file node.py on a port with following command : _python node.py -p 5000_ . This will simulate a node, running on port 5000. You can run another node, on a different port, say 5001. The port numbers are used as addresses to identify nodes.
* **Step 5** : Open the browser and run the servers. 
**Further steps : Create a wallet, if not yet created, or load the previously saved keys. Enter the other nodes on your network using their port numbers. Create a transaction. Mine a new block... and much more.

