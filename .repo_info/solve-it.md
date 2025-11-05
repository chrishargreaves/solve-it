# SOLVE-IT Knowledge Base

This is a generated markdown version of the SOLVE-IT knowledge base. See [GitHub repository](https://github.com/SOLVE-IT-DF/solve-it) for more details.



# Objective Index
- [Find potential digital evidence sources](#find-potential-digital-evidence-sources)
- [Prioritize digital evidence sources](#prioritize-digital-evidence-sources)
- [Preserve digital evidence](#preserve-digital-evidence)
- [Acquire data](#acquire-data)
- [Gain access](#gain-access)
- [Read data from digital evidence storage formats](#read-data-from-digital-evidence-storage-formats)
- [Reduce data under consideration](#reduce-data-under-consideration)
- [Access partitions, volumes and file systems data](#access-partitions,-volumes-and-file-systems-data)
- [Extract artifacts stored by the operating system](#extract-artifacts-stored-by-the-operating-system)
- [Extract artifacts stored by applications](#extract-artifacts-stored-by-applications)
- [Extract artifacts, or content of specific types](#extract-artifacts,-or-content-of-specific-types)
- [Locate potentially relevant content](#locate-potentially-relevant-content)
- [Review content for relevance](#review-content-for-relevance)
- [Detect anti-forensics and other anomalies](#detect-anti-forensics-and-other-anomalies)
- [Establish identities](#establish-identities)
- [Create visualizations](#create-visualizations)
- [Reconstruct events](#reconstruct-events)
- [Conduct research](#conduct-research)
- [Produce documentation](#produce-documentation)

# Objectives and Techniques
<a id="find-potential-digital-evidence-sources"></a>
### Find potential digital evidence sources
*Locate sources of digital evidence that may be relevant to the investigation.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1005 - Crime scene searching](md_content/T1005.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1006 - Digital sniffer dogs](md_content/T1006.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1007 - SyncTriage-based approach](md_content/T1007.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1008 - Profiling network traffic](md_content/T1008.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1009 - Locate cloud account identifiers](md_content/T1009.md)
<a id="prioritize-digital-evidence-sources"></a>
### Prioritize digital evidence sources
*Rank the evidence sources based on their relevance and potential value to the investigation.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1001 - Triage](md_content/T1001.md)
<a id="preserve-digital-evidence"></a>
### Preserve digital evidence
*Ensure the integrity and authenticity of digital evidence is maintained.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1010 - Place device in faraday environment](md_content/T1010.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1011 - Store seized devices in evidence bags](md_content/T1011.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1012 - Hardware write blockers](md_content/T1012.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1013 - Software write blockers](md_content/T1013.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1110 - Preserving reference data](md_content/T1110.md)
<a id="acquire-data"></a>
### Acquire data
*Collect data from the identified evidence sources.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1002 - Disk imaging](md_content/T1002.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1003 - Memory imaging](md_content/T1003.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1004 - Selective data acquisition](md_content/T1004.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1015 - Privacy preserving selective extraction](md_content/T1015.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1016 - Live data collection](md_content/T1016.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1017 - Network packet capture](md_content/T1017.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1018 - Remote data collection](md_content/T1018.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1019 - Mobile backup extraction](md_content/T1019.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1020 - Mobile file system extraction](md_content/T1020.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1022 - Mobile device screenshot based capture](md_content/T1022.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1023 - Cloud data collection using account details](md_content/T1023.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1024 - Cloud data collection via request](md_content/T1024.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1025 - Writing data to a forensic image format](md_content/T1025.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1026 - Writing data in standard archive format](md_content/T1026.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1027 - Data read using JTAG](md_content/T1027.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1028 - Chip-off](md_content/T1028.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1029 - Data read from desoldered eMMC](md_content/T1029.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1030 - Data read from unmanaged NAND](md_content/T1030.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1104 - Collect data using open source intelligence](md_content/T1104.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1111 - Recording system clock offset](md_content/T1111.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1112 - Physical disk identification and removal](md_content/T1112.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1113 - Access internal storage via bootable environment](md_content/T1113.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1114 - Memory Acquisition via Cold Boot Attack](md_content/T1114.md)
<a id="gain-access"></a>
### Gain access
*Attempt to gain access to protected data sources or other restricted data.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1031 - Key recovery from memory](md_content/T1031.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1032 - Side channel](md_content/T1032.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1033 - Extraction of account details from an accessible device](md_content/T1033.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1034 - Brute force attack](md_content/T1034.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1035 - Dictionary attack](md_content/T1035.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1036 - Smudge attack](md_content/T1036.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1037 - Obtain password from suspect](md_content/T1037.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1038 - Rainbow tables](md_content/T1038.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1039 - App downgrade](md_content/T1039.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1040 - Use mobile device exploit](md_content/T1040.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1041 - Pin2Pwn](md_content/T1041.md)
<a id="read-data-from-digital-evidence-storage-formats"></a>
### Read data from digital evidence storage formats
*Access data within digital evidence containers such as disk images, memory dumps, or archive formats.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1042 - Disk image hash verification](md_content/T1042.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1043 - Forensic image format decoding](md_content/T1043.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1044 - Mobile backup decoding](md_content/T1044.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1045 - Decode standard archive format](md_content/T1045.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1102 - Decode data from image from unmanaged NAND](md_content/T1102.md)
<a id="reduce-data-under-consideration"></a>
### Reduce data under consideration
*Filter the data to be considered in the investigation for practical, legal, or privacy protection reasons.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1046 - Privileged material protection](md_content/T1046.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1047 - Hash matching (reduce)](md_content/T1047.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1048 - Privacy protection via partial processing](md_content/T1048.md)
<a id="access-partitions,-volumes-and-file-systems-data"></a>
### Access partitions, volumes and file systems data
*Process core data storage structures such as partitions, volumes, and file systems, recovering content and metadata.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1059 - Identify partitions](md_content/T1059.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1060 - Enumerate allocated files and folders](md_content/T1060.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1061 - Recover non-allocated files](md_content/T1061.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1150 - Recover non-allocated files using residual file metadata](md_content/T1150.md)
    - <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1064 - File carving](md_content/T1064.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1062 - Decryption of encrypted file systems/volumes](md_content/T1062.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1063 - Identify file types](md_content/T1063.md)
<a id="extract-artifacts-stored-by-the-operating-system"></a>
### Extract artifacts stored by the operating system
*Process data stored by the operating system to extract digital forensic artifacts.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1065 - Content indexer examination (OS)](md_content/T1065.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1066 - Log file examination (OS)](md_content/T1066.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1067 - Cloud synchronisation feature examination (OS)](md_content/T1067.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1068 - Recently used file identification (OS)](md_content/T1068.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1083 - Memory examination (OS-level)](md_content/T1083.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1096 - Run programs identification (OS)](md_content/T1096.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1097 - Installed programs identification (OS)](md_content/T1097.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1098 - User account analysis (OS)](md_content/T1098.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1116 - Determine connected devices](md_content/T1116.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1149 - File versioning feature examination](md_content/T1149.md)
<a id="extract-artifacts-stored-by-applications"></a>
### Extract artifacts stored by applications
*Process data stored by the applications to extract digital forensic artifacts.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1069 - Browser examination](md_content/T1069.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1137 - Browser history examination](md_content/T1137.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1138 - Browser cache examination](md_content/T1138.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1139 - Browser session examination](md_content/T1139.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1140 - Browser autofill examination](md_content/T1140.md)
    - <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1141 - Browser bookmarks examination](md_content/T1141.md)
    - <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1142 - Browser downloads examination](md_content/T1142.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1143 - Browser configuration examination](md_content/T1143.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1144 - Browser profile enumeration](md_content/T1144.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1145 - Browser extensions examination](md_content/T1145.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1146 - Browser synchronization feature examination](md_content/T1146.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1147 - Browser cookie examination](md_content/T1147.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1148 - Browser web storage examination](md_content/T1148.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1070 - Email examination](md_content/T1070.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1072 - Chat app examination](md_content/T1072.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1073 - Calendar app examination](md_content/T1073.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1074 - Social network app examination](md_content/T1074.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1075 - Maps/travel app examination](md_content/T1075.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1077 - Photos app examination](md_content/T1077.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1078 - Cloud sync app examination](md_content/T1078.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1105 - Memory examination (application-level)](md_content/T1105.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1107 - Health/Fitness app examination](md_content/T1107.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1108 - Reminders app examination](md_content/T1108.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1109 - Payment app examination](md_content/T1109.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1133 - AI companion app examination](md_content/T1133.md)
<a id="extract-artifacts,-or-content-of-specific-types"></a>
### Extract artifacts, or content of specific types
*Process data to extract artifacts or stored content of specific types.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1021 - Configuration file examination](md_content/T1021.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1052 - Timeline generation](md_content/T1052.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1053 - Entity extraction](md_content/T1053.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1056 - Entity connection enumeration](md_content/T1056.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1071 - Database examination](md_content/T1071.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1076 - Log file examination](md_content/T1076.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1099 - File repair with grafting](md_content/T1099.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1100 - EXIF data extraction](md_content/T1100.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1120 - Automated artifact extraction](md_content/T1120.md)
<a id="locate-potentially-relevant-content"></a>
### Locate potentially relevant content
*Attempt to find digital artifacts relevant to the investigation.*

- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1049 - Keyword searching](md_content/T1049.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1125 - Keyword search (live)](md_content/T1125.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1126 - Keyword search (live) (physical)](md_content/T1126.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1127 - Keyword search (live) (logical)](md_content/T1127.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1124 - Keyword search (indexed)](md_content/T1124.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1121 - Keyword indexing](md_content/T1121.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1122 - Keyword search (case-type wordlists)](md_content/T1122.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1123 - Keyword search (case-specific wordlists)](md_content/T1123.md)
    - <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1151 - Keyword search (over extracted artifacts)](md_content/T1151.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1050 - Hash matching (locate)](md_content/T1050.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1051 - Fuzzy hash matching](md_content/T1051.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1086 - Timeline analysis](md_content/T1086.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1118 - Locate relevant files by path](md_content/T1118.md)
<a id="review-content-for-relevance"></a>
### Review content for relevance
*Review potentially relevant content to determine its significance or meaning.*

- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1054 - Manual content review for relevant material](md_content/T1054.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1055 - File system content inspection](md_content/T1055.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1079 - Audio content analysis](md_content/T1079.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1080 - Video content analysis](md_content/T1080.md)
    - <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1106 - Deep fake detection (video)](md_content/T1106.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1081 - Image content analysis](md_content/T1081.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1082 - Document content analysis](md_content/T1082.md)
<a id="detect-anti-forensics-and-other-anomalies"></a>
### Detect anti-forensics and other anomalies
*Search for indicators of anti-forensic techniques or other anomalies such as malware, which could affect interpretation.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1057 - Search for indicators of steganography](md_content/T1057.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1058 - Search for mismatched file extensions](md_content/T1058.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1128 - Search for indicators of malware](md_content/T1128.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1129 - Search for indicators of clock tampering](md_content/T1129.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1130 - Search for indicators of encrypted data](md_content/T1130.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1131 - Search for indicators of trail obfuscation](md_content/T1131.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1132 - Search for indicators of artifact wiping](md_content/T1132.md)
<a id="establish-identities"></a>
### Establish identities
*Attempt to link data or devices to individuals.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1084 - Extraction of user accounts](md_content/T1084.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1085 - Identify conflation](md_content/T1085.md)
<a id="create-visualizations"></a>
### Create visualizations
*Display information using visual representations to assist with analysis.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1103 - Virtualise suspect system for previewing](md_content/T1103.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1115 - Visualisation of geolocation information](md_content/T1115.md)
<a id="reconstruct-events"></a>
### Reconstruct events
*Use available digital evidence to formulate and test hypotheses about events.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1087 - Location-based event reconstruction](md_content/T1087.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1088 - Connection-based event reconstruction](md_content/T1088.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1117 - Time-based event reconstruction](md_content/T1117.md)
<a id="conduct-research"></a>
### Conduct research
*Conduct research to gain additional knowledge to support the acquisition, extraction, or interpretation of digital evidence.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1089 - Source code review](md_content/T1089.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1090 - Experimentation](md_content/T1090.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1095 - Instrumentation](md_content/T1095.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1101 - Cell site survey](md_content/T1101.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1119 - Automatically scan for artifact changes caused by app updates](md_content/T1119.md)
<a id="produce-documentation"></a>
### Produce documentation
*Create documentation about techniques used and findings.*

- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1014 - Chain of custody documentation](md_content/T1014.md)
- <span style="background-color: #FCE5CD; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1091 - Bookmark artifacts](md_content/T1091.md)
- <span style="background-color: #D9EAD3; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1092 - Produce bookmark-based automated report](md_content/T1092.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1093 - Write expert report](md_content/T1093.md)
- <span style="background-color: #F4CCCC; padding: 8px 10px; border-radius: 2px; display: inline-block;"> </span> [T1094 - Disclosure](md_content/T1094.md)


---

*Markdown generated: 2025-11-05 21:49:38*
