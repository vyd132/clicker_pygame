import view,model,pygame,controller



while True:
    model.clock.tick(60)
    controller.controller()
    view.view()