Space Proof Of Concept 7-9 September 2021
======

**Welcome to SPoC, Space Proof of Concept, a creative and explorative event on how to train AI models in space - the ultimate edge!**

[AI Sweden](www.ai.se), the [Swedish National Space Agency](https://www.rymdstyrelsen.se/en/) and the [RISE Space Data Lab](https://rymddatalabbet.se/) together with you and partners aim to generate PoC:s for space, utilizing the infrastructure in [Edge Lab](https://www.ai.se/en/data-factory/edge-lab) as a simulated space setting.

The event will include inspirational speakers including a keynote by Christer Fuglesang; access to edge devices (simulated satellites); and space data from [Copernicus Satellites](https://www.esa.int/Applications/Observing_the_Earth/Copernicus) in the Edge Lab. 

The main focus of the event will be a 'Collaboraton' - a fusion between hackathon and collaboration. This will provide a creative setting for generating interesting ideas and future projects together. You can test grand ideas with others and accelerate our way to space!

### General event information

Schedule can be found [here](https://sv-se.invajo.com/events/tab/tabId/d9365ce0-d34f-11eb-9e01-63c8b03fbe48/id/60d4eec0-d34c-11eb-a1e6-afb858150bed)
and speakers [here](https://sv-se.invajo.com/events/tab/tabId/97abcad0-d8d9-11eb-9990-93c34932d712/id/60d4eec0-d34c-11eb-a1e6-afb858150bed)

The first part of the event is an open webinar 8-10:45AM 7th of September, if you wish to join please register [here](https://sv-se.invajo.com/events/welcome/id/60d4eec0-d34c-11eb-a1e6-afb858150bed)



Information for collaboration attendees 
======
Please note that the collaboration part of the event, 10:45AM 7th to 5PM 9th of September is **invite only** and specific information about how to attend on-site/remote, slack channels, discord servers, VPN account etc has been sent out separately

At the end of the brainstorming session we will ask you to pair up into groups of 3-7. Our hope is that the brainstorming will lead to a discovery of shared interest and ideas and therefore aim to leave the pairing up to you. If you wish to change group during the event, please notify us in slack (or in person if you are attending on-site). 

## VPN access
VPN account credentials has been sent out via mail, if you have not recieved them or has questions, reach out to kim@ai.se

Please refer to the **VPNAccessGuideForX.pdf** for more detailed information for setting up the VPN connection.

**NOTE:** After you have logged in for the first time trough the vpn, you will need to change from the “default” password. After changing password, you will have the new password on both the VPN and services assigned to you.

Steps:
1. Go to accounts.edgelab.network/auth/realms/edgelab/account/ - requires VPN connection.
2. Login with the password given to you over Email.
3. Go to Signing In and then press Update
4. Change password.
5. Done!

## Equipment/Project setup

We've set up 3 baseline projects for the participants/collaborators to use freely during the event. Each machine has a "fresh" install of either the vendors suggested OS or when that does not applicable, Ubuntu 20.04 LTS. The hardware and networking setup for each project can be modified upon request, e.g. add/remove resources, limit bandwith etc.

Generic user guides for the various hw can be found here:

**Nvidia Jetson AGX Xavier** [documentation and tutorials](https://developer.nvidia.com/embedded/learn/getting-started-jetson)  
**Google Coral** [documentation and tutorials](https://coral.ai/docs/)  
**Raspberry Pi 4** [documentation and tutorials](https://www.raspberrypi.org/learn/)  

To access the projects you will have to connect via VPN (this also applies to those whom are attending on-site)

### Project 1

| IP Address    | Type        | CPU    | RAM      | Storage     |
| ------------- | ------------| ------ | -------- | ----------- |
| 172.25.17.34  | Data VM	    | 4 vCPU | 8GB      | 50GB + Data |
| 172.25.17.35  | VM 1	      | 4 vCPU | 8GB      | 50GB        |
| 172.25.17.36  | VM 2	      | 4 vCPU | 8GB      | 50GB        |
| 172.25.17.47  | Raspberry 1	| 4 CPU  | 4GB      | 16GB        |
| 172.25.17.48  | Raspberry 2	| 4 CPU  | 4GB      | 16GB        |
| 172.25.17.49  | Coral 4	    | 4 CPU  | 8GB      | 32GB        |
| 172.25.17.50  | Xavier 1    | 4 CPU  | 8GB      | 32GB        |
| 172.25.17.51  | Xavier 2    | 8 CPU  | 32GB     | 32GB        |
| 172.25.17.52  | Coral 3	    | 8 CPU  | 32GB     | 32GB        |
	

### Project 2

| IP Address    | Type        | CPU    | RAM      | Storage     |
| ------------- | ------------| ------ | -------- | ----------- | 
| 172.25.17.66  | Data VM	    | 4 vCPU | 8GB      | 50GB + Data |
| 172.25.17.67  | VM 1	      | 4 vCPU | 8GB      | 50GB        |
| 172.25.17.68  | VM 2	      | 4 vCPU | 8GB      | 50GB        |
| 172.25.17.79  | Coral 6	    | 4 CPU  | 4GB      | 16GB        |
| 172.25.17.80  | Coral 5	    | 4 CPU  | 4GB      | 16GB        |
| 172.25.17.81  | Raspberry 3	| 4 CPU  | 8GB      | 32GB        |
| 172.25.17.82  | Raspberry 4	| 4 CPU  | 8GB      | 32GB        |
| 172.25.17.83  | Xavier 4	  | 8 CPU  | 32GB     | 32GB        |
| 172.25.17.84  | Xavier 3	  | 8 CPU  | 32GB     | 32GB        |


### Project 3

| IP Address    | Type        | CPU    | RAM      | Storage     |
| ------------- | ------------| ------ | -------- | ----------- | 
| 172.25.17.98	| Data VM	    | 4 vCPU | 8GB      | 50GB + Data |
| 172.25.17.99	| VM 1	      | 4 vCPU | 8GB      | 50GB        |
| 172.25.17.100	| VM 2	      | 4 vCPU | 8GB      | 50GB        |
| 172.25.17.111	| Coral 8	    | 4 CPU	 | 4GB      | 16GB        |
| 172.25.17.112	| Coral 7	    | 4 CPU	 | 4GB      | 16GB        | 
| 172.25.17.113	| Raspberry 5	| 4 CPU	 | 8GB      | 32GB        |
| 172.25.17.114	| Raspberry 6	| 4 CPU	 | 8GB      | 32GB        |
| 172.25.17.115	| Xavier 5	  | 8 CPU	 | 32GB     | 32GB        |
| 172.25.17.116	| Xavier 6	  | 8 CPU	 | 32GB     | 32GB        |


## Interesting know how that might be useful

Datasets
======
On the Virtual Machine marked with **Data** in your project you'll find the Copernicus datasets under **/mount/copernicus**


