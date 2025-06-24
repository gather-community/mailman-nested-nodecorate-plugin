## Mailman Nested Plugin
This plugin adds 2 enhancements to the processing of nested lists, i.e. where one list is a member of another.  It prevents a child list from doing two things if they have already been done by the parent list:
1. Decoration, i.e. the subject prefix, footer etc.
2. DMARC Mitigation

## Installation
1. Download the code into a directory called nested_nodecorate_plugin
2. In that directory, run 
   
