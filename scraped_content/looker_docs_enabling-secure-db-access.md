# https://cloud.google.com/looker/docs/enabling-secure-db-access

Depth: 3

**Looker-hosted instances** — Many companies prefer to use a Looker-hosted instance for the simplicity, ease of implementation, and reduced support costs. In this case, the data that passes between Looker and the database travels over the public Internet, on shared infrastructure. Consequently, it is important to ensure data security. Use one of the options on this page to ensure that your network can connect securely to your Looker-hosted instance.

**Customer-hosted instances** — Customers who are hosting their own Looker instance may be on the same private network as their database. However, if that is not the case, be sure to secure your data as well, perhaps using the types of options suggested on this page. For an IP address allowlist, add to the allowlist the IP address or addresses where your Looker instance is hosted.

**Note:** The Looker Platform uses a read-only connection for its users to access the minimum amount of data needed to answer questions and only returns the relevant result set. Alternatively, customers can choose to give Looker write-access to their database to take advantage of PDTs (persistent derived tables). This feature lets you define summary tables that Looker will write on your behalf into your database, at a cadence of your choosing.

These are the options for enabling secure database access for your instance, from simplest to most complex:

  * Option 1: IP address allowlist
  * Option 2: SSL encryption
  * Option 3: SSH tunnel

See the following sections for details.

## Option 1: IP address allowlist

The first step is to limit access to your data from the network layer. We recommend granting access to your database only from specific, trusted hosts.

The list of IP addresses that are needed to allow network traffic from your Looker instance can be found on the [**Connections** page](/looker/docs/admin-panel-database-connections) in the **Admin** panel. Click **Public IP Addresses** and copy the IP address(es) that are shown.

![](/static/looker/docs/images/connections-ip-allowlist-2202.png)

**Note:** The **Public IP Addresses** button is not available for [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instances. See the Looker (Google Cloud core) section on this page for more information.

All network traffic from Looker will come from one of the listed IP addresses, depending on the region where your Looker instance is hosted. Prohibiting traffic to your database, except from these and other trusted IP addresses, is an effective way to limit data access.

These allowlist IP addresses also apply to SFTP and SMTP destinations and for LDAP servers that restrict IP traffic. If you are using [custom mail settings for SMTP](/looker/docs/admin-panel-platform-smtp#mail_settings), be sure to add Looker's IP addresses to your SMTP server's IP allowlist. Also, if you want to [deliver content](/looker/docs/scheduling) from Looker to an SFTP server, be sure to add Looker's IP addresses to your SFTP server's IP allowlist or inbound traffic rules. If your LDAP server restricts IP traffic, you will need to add Looker's IP addresses to your LDAP server's IP allowlist or inbound traffic rules.

The complete list of IP addresses for all Looker-hosted environments can be found on this page.

**Note:** You don't need to add all the IP addresses for your region to your allowlist. For the most accurate and condensed list, refer to the **Public IP Addresses** button shown in the **Connections** page in the **Admin** panel.

### Looker (Google Cloud core) instances

If you are using a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance that is set up for public IP or for both public IP and private IP, use the IP address listed in the **Egress Public IP** field on the [**Details** tab](/looker/docs/looker-core-view-console#details_tab) of the **Instances** page in the Google Cloud console.

### Instances hosted on Google Cloud

Looker-hosted instances are hosted on Google Cloud by default. For instances that are hosted on Google Cloud, add to the allowlist the IP addresses that match your [region](/docs/geography-and-regions). 

#### Click here for a full list of IP addresses for instances that are hosted on Google Cloud

#### Moncks Corner, South Carolina, USA (`us-east1`)

  * `34.23.50.137`
  * `35.211.210.64`
  * `35.211.95.55`
  * `35.185.59.100`
  * `34.111.239.102`
  * `35.237.174.17`
  * `34.73.200.235`
  * `35.237.168.216`
  * `34.75.58.123`
  * `35.196.30.110`
  * `35.243.254.166`

#### Ashburn, Northern Virginia, USA (`us-east4`)

  * `34.150.212.9`
  * `34.150.174.54`
  * `34.85.200.217`
  * `35.221.30.177`
  * `35.245.82.73`
  * `34.86.214.226`
  * `35.245.177.112`
  * `35.245.211.109`
  * `34.86.118.239`
  * `34.86.136.190`
  * `35.194.74.185`
  * `34.86.52.188`
  * `35.221.3.163`
  * `35.221.62.218`
  * `34.86.34.135`
  * `35.236.240.168`
  * `35.199.50.237`
  * `34.145.252.255`
  * `35.245.141.42`
  * `35.245.20.16`
  * `34.145.147.146`
  * `34.145.139.22`
  * `34.150.217.20`
  * `35.199.35.176`
  * `35.245.72.35`
  * `34.85.187.175`
  * `35.236.220.225`
  * `34.150.180.94`
  * `4.85.195.168`
  * `34.86.126.124`
  * `34.145.200.8`
  * `34.85.142.95`
  * `34.150.217.96`
  * `35.245.140.36`
  * `34.86.124.234`
  * `35.194.69.239`
  * `35.230.163.26`
  * `35.186.187.48`
  * `34.86.154.134`
  * `34.85.128.250`
  * `35.245.212.212`
  * `35.245.74.75`
  * `34.86.246.187`
  * `34.86.241.216`
  * `34.85.222.9`
  * `34.86.171.127`
  * `34.145.204.106`
  * `34.150.252.169`
  * `35.245.9.213`

#### Council Bluffs, Iowa, USA (`us-central1`)

  * `104.154.21.231`
  * `35.192.130.126`
  * `35.184.100.51`
  * `34.70.128.74`
  * `34.69.207.176`
  * `35.239.118.197`
  * `34.172.2.227`
  * `34.71.191.210`
  * `34.173.109.50`
  * `35.225.65.3`
  * `34.170.192.190`
  * `34.27.97.67`
  * `35.184.118.155`
  * `34.27.58.160`
  * `34.136.4.153`
  * `35.184.8.255`
  * `35.222.218.140`
  * `34.123.109.49`
  * `34.67.240.23`
  * `104.197.72.40`
  * `34.72.128.33`
  * `35.226.158.66`
  * `34.134.4.91`
  * `35.226.210.85`

#### The Dalles, Oregon, USA (`us-west1`)

  * `34.127.41.199`
  * `34.82.57.225`
  * `35.197.66.244`
  * `35.197.64.57`
  * `34.82.193.215`
  * `35.247.117.0`
  * `35.233.222.226`
  * `34.82.120.25`
  * `35.247.5.99`
  * `35.247.61.151`
  * `35.233.249.160`
  * `35.233.172.23`
  * `35.247.55.33`
  * `34.83.138.105`
  * `35.203.184.48`
  * `34.83.94.151`
  * `34.145.90.83`
  * `34.127.116.85`
  * `35.197.35.188`
  * `34.105.127.122`
  * `35.233.191.84`
  * `34.145.93.130`
  * `35.233.178.166`
  * `34.105.18.120`
  * `104.199.118.14`
  * `35.185.228.216`
  * `34.145.16.151`
  * `34.82.91.75`
  * `34.82.142.245`
  * `34.105.35.19`
  * `34.83.231.96`
  * `34.168.230.47`
  * `35.247.46.214`
  * `34.105.44.25`
  * `35.185.196.75`
  * `34.145.39.113`
  * `34.168.121.44`

#### Los Angeles, California, USA (`us-west2`)

  * `35.236.22.77`
  * `35.235.83.177`
  * `35.236.51.71`

#### Montréal, Québec, Canada (`northamerica-northeast1`)

  * `35.234.253.103`
  * `35.203.46.255`
  * `34.152.60.210`
  * `35.203.0.6`
  * `35.234.252.150`
  * `35.203.96.235`
  * `34.152.34.229`
  * `34.118.131.36`
  * `35.203.113.51`

#### London, England, UK (`europe-west2`)

  * `34.105.198.151`
  * `35.246.117.58`
  * `34.142.123.96`
  * `34.89.124.139`
  * `34.89.127.51`
  * `34.105.209.44`
  * `35.242.138.133`
  * `35.197.222.220`
  * `35.189.111.173`
  * `34.105.219.154`
  * `34.105.181.133`
  * `34.89.25.5`
  * `35.246.10.206`
  * `34.105.131.133`
  * `34.142.77.18`
  * `34.89.54.84`
  * `35.189.94.105`
  * `35.246.36.67`
  * `35.234.140.77`
  * `35.242.174.158`
  * `35.197.199.20`
  * `34.89.3.120`
  * `34.105.156.107`
  * `35.246.79.72`
  * `34.105.139.38`
  * `34.105.147.157`
  * `34.105.195.129`
  * `34.105.194.210`
  * `34.142.79.123`
  * `34.142.55.58`
  * `34.142.85.249`
  * `34.105.148.38`
  * `35.246.100.66`
  * `35.246.3.165`
  * `34.105.176.209`
  * `35.189.95.167`
  * `34.89.55.2`

#### Frankfurt, Germany (`europe-west3`)

  * `35.242.243.255`
  * `34.159.247.211`
  * `35.198.128.126`
  * `34.159.10.59`
  * `34.159.72.77`
  * `34.159.224.187`
  * `34.89.159.138`
  * `34.159.253.103`
  * `34.159.244.43`
  * `35.246.162.187`
  * `34.89.141.190`
  * `34.159.65.106`
  * `34.159.197.31`
  * `34.89.194.134`
  * `34.159.252.155`
  * `34.141.65.216`
  * `34.159.124.62`
  * `35.246.130.213`
  * `34.89.206.21`
  * `34.89.185.201`
  * `34.159.171.46`
  * `35.246.217.228`
  * `35.242.236.115`
  * `34.159.148.253`

#### Mumbai, India (`asia-south1`)

  * `35.200.234.34`
  * `34.100.205.37`
  * `34.93.225.12`
  * `34.93.221.137`
  * `35.244.24.198`
  * `35.244.52.179`

#### Eemshaven, Netherlands (`europe-west4`)

  * `35.204.118.28`
  * `35.204.216.7`
  * `34.90.52.191`
  * `35.204.176.29`
  * `34.90.199.95`
  * `34.90.145.226`
  * `34.141.162.7`
  * `35.204.56.189`
  * `35.204.11.229`
  * `34.34.66.131`
  * `34.32.195.89`
  * `34.32.173.138`

#### Changhua County, Taiwan (`asia-east1`)

  * `104.199.206.209`
  * `34.80.173.212`
  * `35.185.137.114`

#### Tokyo, Japan (`asia-northeast1`)

  * `34.85.3.198`
  * `34.146.68.203`
  * `34.84.4.218`

#### Jurong West, Singapore (`asia-southeast1`)

  * `34.143.210.116`
  * `34.143.132.206`
  * `34.87.134.202`
  * `34.101.158.88`
  * `34.101.157.238`
  * `34.101.184.52`

#### Jakarta, Indonesia (`asia-southeast2`)

  * `34.101.158.88`
  * `34.101.157.238`
  * `34.101.184.52`

#### Sydney, Australia (`australia-southeast1`)

  * `34.87.195.36`
  * `34.116.85.140`
  * `34.151.78.48`
  * `35.189.13.29`
  * `35.189.9.81`
  * `35.244.68.217`

#### Osasco (São Paulo), Brazil (`southamerica-east1`)

  * `34.151.199.201`
  * `35.199.122.19`
  * `34.95.180.122`
  * `34.95.168.38`
  * `34.151.235.241`
  * `34.95.181.19`
  * `35.199.91.120`
  * `35.247.197.109`
  * `35.199.86.48`
  * `35.199.106.166`
  * `35.198.1.191`
  * `35.247.235.128`
  * `35.247.211.2`
  * `35.247.200.249`
  * `34.95.177.253`