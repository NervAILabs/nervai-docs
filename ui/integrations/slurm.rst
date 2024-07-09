================================
DFKI Deep Learning Slurm Cluster
================================

`Deutsches Forschungszentrum für Künstliche Intelligenz (DFKI) <https://dfki.de>`_ provides their members a powerful Slurm cluster for deep learning experiments. You can link your cluster account with VisualML to train your networks on the DFKI cluster. For more information about the cluster, please see the `cluster documentation here <https://pegasus.dfki.de/docs/>`_.

To integrate your DFKI Slurm cluster account, follow these steps:

1. Navigate to the **Settings** menu.
2. Select the **Integration** tab.
3. Under the Integration tab, you will find an option to link your DFKI Slurm cluster account by providing:
   - **DFKI Slurm username**
   - **DFKI Slurm password**
   - **VisualML password**

.. image:: /images/integrations/slurm.png
   :alt: User Interface for DFKI Slurm Cluster Integration
   :align: center

**Important:** For privacy, we are not storing the passwords in plain text for DFKI. Your password is end-to-end encrypted.

**Note:** To run jobs on the cluster, you need to integrate your GitHub account as well.