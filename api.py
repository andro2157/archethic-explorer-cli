from connection import con

def getLastTransaction(address):
    return con.executeQuery("""
        query {
            lastTransaction(address: "%s") {
                address
            }
        }
    """ % address)["data"]["lastTransaction"]["address"]

def getBalance(address):
    return con.executeQuery("""
        query {
            balance(address: "%s") {
                token {
                    address,
                    amount,
                    tokenId
                },
                uco
            }
        }
    """ % address)["data"]["balance"]

def getToken(address, vars = "decimals, genesis, id, name, properties, supply, symbol, type"):
    return con.executeQuery("""
        query {
            token(address: "%s") {
                %s
            }
        }
    """ % (address, vars))["data"]["token"]

def getNearestEndpoints():
    return con.executeQuery("""
        query {
            nearestEndpoints {
                ip, port
            }
        }
    """)["data"]["nearestEndpoints"]

def getOracleData(timestamp = None):
    if timestamp == None:
        return con.executeQuery("""
            query {
                oracleData {
                    services {
                        uco {
                            eur, usd
                        }
                    },
                    timestamp
                }
            }
        """)["data"]["oracleData"]
    else:
        return con.executeQuery("""
            query {
                oracleData(timestamp: %d) {
                    services {
                        uco {
                            eur, usd
                        }
                    },
                    timestamp
                }
            }
        """ % timestamp)["data"]["oracleData"]

def getTransactions(page = None):
    if page == None:
        return con.executeQuery("""
            query {
                transactions {
                    address,
                    type,
                    validationStamp {
                        timestamp
                    }
                }
            }
        """)["data"]["transactions"]
    else:
        return con.executeQuery("""
            query {
                transactions(page: %d) {
                    address,
                    type,
                    validationStamp {
                        timestamp
                    }
                }
            }
        """ % page)["data"]["transactions"]

def getTransactionDateAndType(address):
    return con.executeQuery("""
        query {
            transaction(address: "%s") {
                type,
                validationStamp {
                    timestamp
                }
            }
        }
    """ % address)["data"]["transaction"]

def getTransaction(address):
    return con.executeQuery("""
        query {
            transaction(address: "%s") {
                chainLength,
                data {
                    ledger {
                        token {
                            transfers {
                                amount,
                                to,
                                tokenAddress,
                                tokenId
                            }
                        },
                        uco {
                            transfers {
                                amount,
                                to
                            }
                        }
                    },
                    content,
                    recipients
                },
                inputs {
                    amount,
                    from,
                    spent,
                    timestamp,
                    tokenAddress,
                    tokenId,
                    type
                },
                type,
                validationStamp {
                    ledgerOperations {
                        fee,
                        transactionMovements {
                            amount,
                            to,
                            tokenAddress,
                            tokenId,
                            type
                        },
                        unspentOutputs {
                            amount,
                            from,
                            tokenAddress,
                            tokenId,
                            type
                        }
                    },
                    timestamp
                },
                version
            }
        }
    """ % address)["data"]["transaction"]

def getNodes():
    return con.executeQuery("""
        query {
            nodes {
                authorizationDate,
                authorized,
                available,
                averageAvailability,
                enrollmentDate,
                firstPublicKey,
                geoPatch,
                ip,
                lastPublicKey,
                networkPatch,
                originPublicKey,
                port,
                rewardAddress
            }
        }
    """)["data"]["nodes"]

def getTransactionChain(address, pagingaddress = None):
    if pagingaddress == None:
        return con.executeQuery("""
            query {
                transactionChain(address: "%s") {
                    address,
                    type,
                    validationStamp {
                        timestamp
                    }
                }
            }
        """ % address)["data"]["transactionChain"]
    else:
        return con.executeQuery("""
            query {
                transactionChain(address: "%s", pagingAddress: "%s") {
                    address,
                    type,
                    validationStamp {
                        timestamp
                    }
                }
            }
        """ % (address, pagingaddress))["data"]["transactionChain"]

def getNetworkTransactions(type, page = None):
    if page == None:
        return con.executeQuery("""
            query {
                networkTransactions(type: "%s") {
                    address,
                    type,
                    validationStamp {
                        timestamp
                    }
                }
            }
        """ % type)["data"]["networkTransactions"]
    else:
        return con.executeQuery("""
            query {
                networkTransactions(page: %d, type: "%s") {
                    address,
                    type,
                    validationStamp {
                        timestamp
                    }
                }
            }
        """ % (page, type))["data"]["networkTransactions"]