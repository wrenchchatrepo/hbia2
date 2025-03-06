# https://cloud.google.com/looker/docs/testing-db-connectivity

Depth: 3

When troubleshooting a new environment, it is often helpful to isolate the various components in play and test them in isolation as simply as possible.

To test the connectivity between your Looker server and your database, you can use Telnet on your Looker server to create a simple TCP connection. The advantage of using Telnet is that is extremely simple. There are no configuration files to modify and no authentication is required. Telnet either makes the connection or it does not.

Once you know that the database is accessible, you can move on to testing via applications such as your database's native client, or Looker.

## Installing Telnet

Some hosts may come with Telnet pre-installed. To test this, run this command on your Looker server:
    
    
    telnet ?
    

You should see something like this:
    
    
    usage: telnet [-l user] [-a] [-s src_addr] host-name [port]
    

If you get a "command not found" error, you will need to install Telnet.

On Ubuntu:
    
    
    sudo apt-get install telnet
    

On Redhat/CentOS:
    
    
    yum install telnet
    

## Default ports

You will need to know on which port your database is running. The following table lists the default ports for a number of platforms, although your database may be configured to run on a different port. Consult your database administrator.

Platform | Port  
---|---  
Amazon Redshift | 5439  
GreenPlum | 5432  
Microsoft SQL Server (MSSQL) | 1433  
MySQL | 3306  
Oracle | 1521  
PostgreSQL | 5432  
Vertica | 5433  
  
## Connecting to your database with Telnet

To test the connection to your database, run the `telnet hostname port` on your Looker server. For example, if you are running MySQL on the default port and your database name is **mydb** , the command would be `telnet mydb 3306`.

If the connection is working, you will see something similar to this:
    
    
    Trying 10.10.10.10...
    Connected to mydb.
    Escape character is '^]'.
    

If the connection is NOT working, you will see something like one of these:
    
    
    Trying 10.10.10.10...
    telnet: Unable to connect to remote host: Connection timed out
    
    
    
    Trying 127.0.0.1...
    telnet: Unable to connect to remote host: Connection refused
    
    
    
    telnet: could not resolve mydb/telnet: Name or service not known
    

## Troubleshooting

If the Telnet check is not successful, consider the following:

  * Is the hostname correct?
  * Are the database and Looker server configured to allow the network traffic between them? Check any installed firewall software on both hosts.
  * Are all the networks between the Looker server and the database hosts configured to allow the network traffic? Check firewalls and network Access Control Lists (ACLs).
  * Are all the networks between the Looker server and the database hosts configured correctly to route traffic between the hosts?
  * Is the database server running, is it listening on the correct port, and is it configured to allow connections from the Looker server?

## Next steps

If you are able to Telnet from your Looker server to your database server's port, you can rule out basic connectivity issues. The next step is to [create a Looker database connection](/looker/docs/connecting-to-your-db).