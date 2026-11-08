Making a Pull Request
=====================

Actions to take on each PR that modifies the schema and does not prepare the schema for a public release
(this is also in the `GitHub PR template`_):

If the current schema version on "main" is a public release, then:

1. Update the version string in ``docs/source/conf.py`` and ``common/namespace.yaml`` to the next version with the
   suffix "-alpha"
2. Add a new section in the release notes for the new version with the date "Upcoming"

Always:

1. Add release notes for the PR to ``docs/source/hdmf_common_release_notes.rst`` and/or
   ``docs/source/hdmf_experimental_release_notes.rst``

Documentation or internal changes to the repo (i.e., changes that do not affect the schema files)
do not need to be accompanied with a version bump or addition to the release notes.

.. _`GitHub PR template`: https://github.com/hdmf-dev/hdmf-common-schema/blob/main/.github/PULL_REQUEST_TEMPLATE.md


Merging PRs and Making Releases
===============================

**Public release**: a tagged release of the schema. The version string MUST NOT have a suffix indicating a pre-release,
such as "-alpha". The current "dev" branch of HDMF and all HDMF releases MUST point to a public release of
hdmf-common-schema. All schema that use hdmf-common-schema as a submodule MUST also point only to public releases.

**Internal release**: a state of the schema "main" branch where the version string ends with "-alpha".

The default branch of hdmf-common-schema is "main". **The "main" branch holds the bleeding edge version of
the hdmf-common schema specification.**

PRs should be made to "main". Every PR should include an update to the namespace release notes
(``docs/source/hdmf_common_release_notes.rst`` and/or ``docs/source/hdmf_experimental_release_notes.rst``).
If the current version is a public release, then the PR should also update the version of the schema in two places:
``docs/source/conf.py`` and ``common/namespace.yaml``. The new version should be the next bugfix/minor/major version
of the schema with the suffix "-alpha". For example, if the current schema on "main" has version "2.2.0",
then a PR implementing a bug fix should update the schema version from "2.2.0" to "2.2.1-alpha". Appending the "-alpha"
suffix ensures that any person or API accessing the default "main" branch of the repo containing an internal release
of the schema receives the schema with a version string that is distinct from public releases of the schema. If the
current schema on "main" is already an internal release, then the version string does not need to be updated unless
the PR requires an upgrade in the version (e.g., from bugfix to minor).

HDMF should contain a branch and PR that tracks the "main" branch of hdmf-common-schema. Before
a public release of hdmf-common-schema is made, this HDMF branch should be checked to ensure that when the new release
is made, the branch can be merged without issue.

Immediately prior to making a new public release, the version of the schema should be updated to remove the "-alpha"
suffix and the documentation and release notes should be updated as needed (see next section).

The current "dev" branch of HDMF and all HDMF releases MUST always point to a public release of hdmf-common-schema. If
a public release contains an internally released version of hdmf-common-schema, e.g., from an untagged commit on the
"main" branch, then it will be difficult to find the version (commit) of hdmf-common-schema that was used to create
an HDMF file when the schema is not cached.

Making a Release Checklist
==========================

Before merging:

1. Update requirements versions as needed
2. Update legal file dates and information in ``Legal.txt``, ``license.txt``, ``README.md``, ``docs/source/conf.py``,
   and any other locations as needed
3. Update ``README.md`` as needed
4. Update the version string in ``docs/source/conf.py`` and ``common/namespace.yaml`` (remove "-alpha" suffix)
5. Update ``docs/source/conf.py`` as needed
6. Update release notes (set release date) in `docs/source/hdmf_common_release_notes.rst`,
   `docs/source/hdmf_experimental_release_notes.rst`, and any other docs as needed
7. Test docs locally (``cd docs; make fulldoc``) where the hdmf-common-schema submodule in the local version of HDMF
   is fully up-to-date with the head of the main branch.
8. Push changes to a new PR and make sure all PRs to be included in this release have been merged. Add
   ``?template=release.md`` to the PR URL to auto-populate the PR with this checklist.
9. Check that the readthedocs build for this PR succeeds (build latest to pull the new branch, then activate and
   build docs for new branch): https://readthedocs.org/projects/hdmf-common-schema/builds/

After merging:

1. Create a new git tag. Pull the latest main branch locally, run ``git tag [version] --sign``, copy and paste the
   release notes into the tag message, and run ``git push --tags``.
2. On the `GitHub tags`_ page, click "..." -> "Create release" for the new tag on the right side of the page.
   Copy and paste the release notes into the release message, update the formatting if needed (reST to Markdown),
   and set the title to the version string.
3. Check that the readthedocs "latest" and "stable" builds run and succeed. Delete the readthedocs build for the
   merged PR. https://readthedocs.org/projects/hdmf-common-schema/builds/
4. Update the HDMF submodule in the HDMF branch corresponding to this schema version to point to the tagged commit.

This checklist can also be found in the `GitHub release PR template`_.

The time between merging this PR and creating a new public release should be minimized.

.. _`GitHub tags`: https://github.com/hdmf-dev/hdmf-common-schema/tags
.. _`GitHub release PR template`: https://github.com/hdmf-dev/hdmf-common-schema/blob/main/.github/PULL_REQUEST_TEMPLATE/release.md
