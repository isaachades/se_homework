public class Consumer {
    public static void main(String[] args) {
        HotspotOrder order1 = new CDOrderFac().getOrder();
        HotspotOrder order2 = new CQOrderFac().getOrder();

        order1.name();
        order2.name();
    }
}
