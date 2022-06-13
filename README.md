
senaite.indexer
===============

This is a Plone add-on that allows for indexing/re-indexing of SENAITE LIMS catalogs. It can also be used to create new catalogs with new indexes. This is currently done inside the [catalog.xml](src/senaite/indexer/profiles/default/catalog.xml) file.

Installation
------------

Install senaite.indexer by adding it to your buildout::

    [buildout]

    ...

    eggs =
        senaite.indexer


and then running ``bin/buildout``

List of all packaged indexes and catalogs
-----------------------------------------

* `getClientID` on the `portal_catalog` as a `FieldIndex`; this make's it possible to search SENAITE LIMS for a client using their external client `id`.


Contribute
----------

- Issue Tracker: https://github.com/mekomsolutions/senaite.indexer/issues
- Source Code: https://github.com/mekomsolutions/senaite.indexer


Support
-------

If you are having issues, please let us know.