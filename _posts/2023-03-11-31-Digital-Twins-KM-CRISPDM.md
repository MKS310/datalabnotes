---
title: "Paper Review: Digital Twins for Retrofit in Aviation via Model-Driven Data Handling"
author: Maggie Conroy
categories: DigitalTwin
layout: post
---

# Paper Review: Supporting Digital Twins for the Retrofit in Aviation by a Model-Driven Data Handling
## Knowledge Management via MBSE and Graph DBs Enables the Creation of a Descriptive Digital Twin

It is sometimes said that a digital twin can start as simply as digitizing the owner's manual for a piece of equipment. But that can be easier said than done.  
  
Some organizations have adopted good Knowledge Management practices over time, but for equipment that's been around for a while, this is not the case 😳  
  
This paper[1] proposes a methodical solution to a common problem: When retrofitting old equipment (airplanes in this case) with new tech, you will find documentation scattered across filesystems and known only to subject matter experts.  
  
According to Experts:  
  
⛔️ There are a multitude of single documents, often PDF files or even analog paper documents, and no simple holistic description of the actual current state of a piece of equipment  
⛔️ Documentation is fragmented and incomplete  
⛔️ Descriptive documents, including circuit and system diagrams, are rarely provided as digital models  
⛔️ Some information is stored solely in printed media. Relations between documents can be known through experience and are not explicitly available  
  
This paper draws attention to this problem and mentions some limitations of current data handling practices, such as Model-Based Systems Engineering (MBSE) which uses centralized graphical SysML.  
  
"Currently, no independent file format has been established, and the authoring systems include only a few to no application programming interfaces (APIs)."  
  
This limitation makes it hard to access, use and analyze the system information.  
  
But, the authors note that lessons can be learned from data science and utilize Graph Databases and CRISP-DM to overcome the limitations, thus combining best practices from MBSE and Data Science 🤝  
  
"With model-based documentation originating from MBSE and data science’s CRISP-DM methodology, two approaches were identified, which can support the data handling regarding the retrofit in aviation."  
  
The article examines the hypothesis:  
  
"A model-based approach documenting known relevant meta-information and relations in combination with techniques originating from the data sciences can provide a strategy to iteratively create virtual representations of aircraft aggregating the relevant information for the specific aircraft, and thus supporting the engineers planning and performing the cabin retrofit. An overarching procedure enabling the occurring (meta-) information within the depicted scenario iteratively supports the implementation of the presented concept."  
  
⭐️ They found that they could iterate through the first 4 phases of CRISP-DM to build a comprehensive system model. Then, traditional MBSE SysML knowledge stores could be enriched with info and ported to a Graph Database (like Neo4j) which provides ⚡️𝐈𝐧𝐭𝐞𝐫𝐨𝐩𝐞𝐫𝐚𝐛𝐢𝐥𝐢𝐭𝐲⚡️ (emphasis because this is one of the known challenges for Digital Twins).  
  
👏 Authors: [Fabian Laukotka](https://www.linkedin.com/in/ACoAACfRHWEBiKNlgzpG9QZgYyXJIoLJOfJOnnc), Dieter Krause  
  
[My LinkedIn Post](https://www.linkedin.com/posts/margaret-schweihs_digitaltwins-mbse-crispdm-activity-7040216889167384576-L9_8?utm_source=share&utm_medium=member_desktop)

## Tags
#digitaltwins #crispdm #mbse #graphdatabases 

## References

[1] F. N. Laukotka and D. Krause, “Supporting Digital Twins for the Retrofit in Aviation by a Model-Driven Data Handling,” _Systems_, vol. 11, no. 3, p. 142, Mar. 2023, doi: 10.3390/systems11030142.