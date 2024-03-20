=================================
Building the Configuration File
=================================


.. code-block:: python

    from visualml.mm import MMPoseUtils

    @app.route('/create_mmpose_config', methods=['GET'])
    def create_mmpose_config():
        backbones = MMPoseUtils.get_backbones()
        heads = MMPoseUtils.get_heads()
        losses = MMPoseUtils.get_losses()
        return redirect(url_for('create_mmpose_config',
                                backbones=backbones,
                                heads=heads,
                                losses=losses))