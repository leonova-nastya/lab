class OperationCommand implements Command {
    private String operation;

    public OperationCommand(String operation) {
        this.operation = operation;
    }

    @Override
    public void execute() {
        System.out.println("Operation pressed: " + operation);
    }
}
