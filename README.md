# Mailman Plugin for Nested lists


This plugin adds 2 enhancements to the processing of nested lists,
i.e. where one list is a member of another. It prevents a child list
from doing two things if they have already been done by the parent
list: decoration and DMARC mitigation. 

## Setup

In order to start using this repo, start by cloning this repo to create a new
package::

```
  $ git clone https://github.com/gather-community/mailman-nested-plugin nesed-nodecorate-plugin
  $ cd nested-nodecorate-plugin
```
Install it in a Python virtualenv using``pip``::
```
  $ python3 -m venv venv
  $ source venv/bin/activate
  (venv) $ pip install -e .
```
## Activate plugin in Mailman Core

In order to activate the plugin in Mailman Core, add the following config to
``mailman.cfg``::

```
## Plugin configuration.
[plugin.nested_nodecorate_plugin]
class: nested_nodecorate_plugin.NestedNodecoratePlugin
enabled: yes
```

## Using the Plugin

To use the plugin, go to the Postorius list panel and the section
`Alter Messages`.  Set the Pipeline to `nested-nodecorate-pipeline`.

Note that `Include RFC2369 headers` must be on in order for the plugin
to work properly.
