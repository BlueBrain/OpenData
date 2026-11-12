.. _hdmf_common_release_notes:

hdmf-common Release Notes
=========================

1.10.0 (July 20, 2026)
----------------------
- Changed ``MeaningsTable.target`` from a link to an object-reference attribute (``dtype`` with
  ``reftype: object``, ``target_type: VectorData``). This matches ``VectorIndex.target`` and
  ``DynamicTableRegion.table``, which use object references to point at a co-located dataset within
  table machinery. This is a breaking change for files written with the 1.9.0 definition of
  ``MeaningsTable``.

1.9.0 (January 29, 2026)
------------------------
- Changed the dtype of ``ElementIdentifiers`` and ``DynamicTableRegion`` from "int" to "int32". Under HDMF
  schema language 2.x, "int" means "int32" so this change has no functional impact, except when displaying the
  spec, such as in error messages.
- Added ``MeaningsTable``, a table for storing meanings for values in linked ``VectorData`` objects.
  This is useful for annotating categorical data stored in a ``DynamicTable``. Added a group named "meanings_tables"
  to ``DynamicTable`` to hold ``MeaningsTable`` objects that provide meanings for ``VectorData`` columns in the
  ``DynamicTable``.
- Minor changes to data type docstrings to improve clarity.
- Promoted ``HERD`` from the HDMF-experimental namespace to a stable data type in the HDMF-common
  namespace.

1.8.0 (August 4, 2023)
----------------------
- No change in the hdmf-common namespace. See :ref:`here <hdmf_experimental_release_notes>` for changes to the
  hdmf-experimental namespace.

1.7.0 (June 22, 2023)
---------------------
- No change in the hdmf-common namespace. See :ref:`here <hdmf_experimental_release_notes>` for changes to the
  hdmf-experimental namespace.

1.6.0 (May 3, 2023)
-------------------
- No change in the hdmf-common namespace. See :ref:`here <hdmf_experimental_release_notes>` for changes to the
  hdmf-experimental namespace.

1.5.1 (January 10, 2022)
------------------------
- No change in the hdmf-common namespace. See :ref:`here <hdmf_experimental_release_notes>` for changes to the
  hdmf-experimental namespace.

1.5.0 (April 19, 2021)
----------------------
- Added ``AlignedDynamicTable``, which defines a ``DynamicTable`` that supports storing a collection of sub-tables.
  Each sub-table is itself a ``DynamicTable`` that is aligned with the main table by row index. Each sub-table
  defines a sub-category in the main table effectively creating a table with sub-headings to organize columns.

1.4.0 (March 29, 2021)
-------------------------

Summary: In 1.4.0, the HDMF-experimental namespace was added, which includes the ``ExternalResources`` and ``EnumData``
data types. Schema in the HDMF-experimental namespace are experimental and subject to breaking changes at any time.
``ExternalResources`` was changed to support storing both names and URIs for resources. The ``VocabData`` data type was
replaced by ``EnumData`` to provide more flexible support for data from a set of fixed values.

- Added ``EnumData`` for storing data that comes from a set of fixed values. This replaces ``VocabData`` which could
  hold only string values. Also, ``VocabData`` could hold only a limited number of elements (~64k) when used with the
  HDF5 storage backend. ``EnumData`` gets around these restrictions by using an untyped dataset (VectorData) instead of
  a string attribute to hold the enumerated values.
- Removed ``VocabData``.
- Renamed the "resources" table in ``ExternalResources`` to "entities".
- Created a new "resources" table to store the name and URI of the ontology / external resource used by the "entities"
  table in ``ExternalResources``.
- Renamed fields in ``ExternalResources``.
- Added "entities" dataset to ``ExternalResources``. This is a row-based table dataset to replace the functionality of
  the "resources" dataset in ``ExternalResources``.
- Changed the "resources" dataset in ``ExternalResources`` to store the name and URI of the ontology / external
  resource used by the "entities" dataset in ``ExternalResources``.
- Added HDMF-experimental namespace.
- Moved ``ExternalResources`` and ``EnumData`` to HDMF-experimental.

1.3.0 (December 2, 2020)
-------------------------

- Add data type ``ExternalResources`` for storing ontology information / external resource references. NOTE: this
  data type is in beta testing and is subject to change in a later version.
- Changed dtype for datasets within ``CSRMatrix`` from 'int' to 'uint'. Negative values do not make sense for these
  datasets.

1.2.1 (November 4, 2020)
------------------------

- Update software process documentation for maintainers.
- Fix missing data_type_inc for ``CSRMatrix``. It now has ``data_type_inc: Container``.
- Add ``hdmf-schema-language`` comment at the top of each yaml file.
- Add ``SimpleMultiContainer``, a Container for storing other Container and Data objects together

1.2.0 (July 10, 2020)
------------------------

- Add software process documentation.
- Fix missing dtype for ``VectorIndex``.
- Add new ``VocabData`` data type.
- Move ``Data``, ``Index``, and ``Container`` to base.yaml. This change does not functionally change the schema.
- ``VectorIndex`` now extends ``VectorData`` instead of ``Index``. This change allows ``VectorIndex`` to index other
  ``VectorIndex`` types.
- The ``Index`` data type is now unused and has been removed.
- Fix documentation for ragged arrays.

1.1.3 (January 21, 2020)
------------------------

- Fix missing 'shape' and 'dims' key for types ``VectorData``, ``VectorIndex``, and ``DynamicTableRegion``.

1.1.2 (January 9, 2020)
-----------------------

- Fix version number in namespace.yaml and docs

1.1.1 (January 9, 2020)
-----------------------

- Support for ReadTheDocs continuous documentation was added, and legal/license documents were also added. The schema is
  unchanged.

1.1.0 (January 3, 2020)
-----------------------

- The 'colnames' attribute of ``DynamicTable`` changed from data type 'ascii' to 'text'.
- Improved documentation and type docstrings.

1.0.0 (September 26, 2019)
--------------------------

Initial release.
