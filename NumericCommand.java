class NumericCommand implements Command {
    private int number;

    public NumericCommand(int number) {
        this.number = number;
    }

    @Override
    public void execute() {
        System.out.println("Number pressed: " + number);
    }
}
