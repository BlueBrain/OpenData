.. _hdmf_experimental_release_notes:

hdmf-experimental Release Notes
===============================

0.6.0 (January 29, 2026)
------------------------
- Promoted ``HERD`` to a stable data type in the HDMF-common namespace. See :ref:`here <hdmf_common_release_notes>` for details.

0.5.0 (August 4, 2023)
----------------------
- Updates ``ExternalResources`` to have a uniform name throughout the codebase and the literature, which is now ``HERD``
  (HDMF External Resources Data).
- Fixed schema bug regarding the missing quote.

0.4.0 (June 22, 2023)
---------------------
- In the experimental ``ExternalResources``, added a ``entity_keys`` table and removed ``keys_idx`` from the ``entities`` table.

0.3.0 (May 3, 2023)
-------------------
- In the experimental ``ExternalResources``, added a ``files`` table, removed the ``resources`` table, and adjusted
  existing columns.

0.2.0 (January 10, 2022)
------------------------
- In the experimental ``ExternalResources``, added ``relative_path`` field to the "objects" table dtype. This is used in
  place of the previous ``field`` field representing the relative path to get to the dataset/attribute from the object.
  The previous ``field`` field will be used to represent a compound type field name if the dataset/attribute is a
  compound dtype.
- Updated contributors.

0.1.0 (March 29, 2021)
----------------------
- See the release notes for :ref:`hdmf-common 1.4.0 <hdmf_common_release_notes>` for details.
