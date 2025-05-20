class CustomCommand implements Command {
    private Runnable action;

    public CustomCommand(Runnable action) {
        this.action = action;
    }

    @Override
    public void execute() {
        action.run();
    }
}
