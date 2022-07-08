### Explanation
This program generates the list of clients who can migrate per released feature in a migration roadmap, e.g.:
After feature A client 1,2,3 can migrate
After feature B client 4,5 can migrate (additionally)
etc
Consequently, the associated subscription quantity (e.g. # users) and MRR can be mapped over time.

It is based on an input file containing all clients and requests a roadmap (by entering a sequence of features).

### Context
This is a helper program to the migration-roadmap-generator, which optimises the roadmap for optimal migration requirements.
Since the 'optimised' roadmap might neglect certain factors, it might be useful to investigate the impact of an adjusted roadmap.
