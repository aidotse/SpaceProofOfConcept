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

**Day 1**  
8.15-8.25 Intro by AI Sweden & the Swedish National Space Agency  
8.25-8.40 Fredrik Bruhn - Unibap - About Spacecloud & more  
8.40-8.55 Kim Henrikson - Zenseact/AI Sweden - Egde Lab   
8.55-9.00 Short break  
9.00-9.15 Evgenia Novikova - Smartilizer - About Federated frameworks and tools  
9.15-9.45 Christer Fuglesang - KTH -   
9.45-9.50 Short break  
9.50-10.10 Tina & Tom Sjögren - Pythomspace  
10.10-10.20 Massimiliano Pastena - European Space Agency    
10.20-10.35 Sorin Cheran - Hewlett Packard Enterprise - Swarm Learning  
10.35-10.45 Q&A and sum-up  

**Open webinar transitions into invite only session**    

10.45-12.00 Collaboraton kick-off brainstorming session (on site & remote)

12-13 LUNCH BREAK

13.00-16.30 Start of Collaboraton with free experimentation and exploration in the Egde Lab.  

13.00-13:30 Deep dive into the edge lab infrastructure and Q&A to get everybody started - Kim/Leo

? Afternoon HPE Swarm learning walkthrough

16.30-17.30 After Work session - with **Tom and Tina from Pythomspace calling in live at 17.00**  

**Day 2**  
08.00-17.00 Collaboraton continues (By invite and application only, on site & remote)

09.00-09.45 Tobias Edman -  Rymdstyrelsen giving a data walkthrough.

During the day, representatives from Smartilizer, HPE, Unibap and AI Sweden will be available for brainstorming and support on Slack.


**Day 3**  
08:00-15:00 Continuation of Collaboraton - by invite and application only (on site & remote)

**15.00 the event opens up to the public again**  

15.00-17.00 Conclusion, wrap up and sharing of the PoC:s (open webinar)



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

All the HW are actually part of the same network infrastructure, but are segmented into vlans. (sidenote: It is possible to configure all communication paths including routing federation communication via 5G, 4G, Wifi etc. But for the event we have skipped that part to make exploration easier.)

Generic user guides for the various hw can be found here:

**Nvidia Jetson AGX Xavier** [documentation and tutorials](https://developer.nvidia.com/embedded/learn/getting-started-jetson)  
**Google Coral** [documentation and tutorials](https://coral.ai/docs/)  
**Raspberry Pi 4** [documentation and tutorials](https://www.raspberrypi.org/learn/)  

(To access the projects you will have to connect via VPN (this also applies to those whom are attending on-site))

### Project 1

IP Range 172.25.17.32/27  
Gateway: 172.25.17.33

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

IP Range 172.25.17.64/27  
Gateway: 172.25.17.65

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

IP Range 172.25.17.96/27  
Gateway: 172.25.17.97

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

## Other resources that can be added to your project upon request
Nvidia Jetson AGX Xavier & Drive PX2  
Google Coral  
Raspberry Pi 4  
HPE EdgeLine1000 with Tesla T4 GPU [generic specs](https://h20195.www2.hpe.com/v2/getdocument.aspx?docname=c05211199)   
Comino Grando RM with **Nvidia A100** / 3975WX / 256GB / 2TB NVMe [generic specs](https://grando.ai/choose-a-gpu-machine-for-ai-deep-learning/#grando-rm)   
Virtual Machines (mainly CPU based)  

# Interesting know how that might be useful

Datasets
======
On the Virtual Machine marked with **Data** in your project you'll find the Copernicus datasets under **/mount/copernicus**


Tips & Tricks
======
Here are some nice [demos](https://coral.ai/docs/dev-board/get-started/#flash-the-board) for the Google Coral's thats nice to start with 
