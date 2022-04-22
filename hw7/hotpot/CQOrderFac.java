public class CQOrderFac implements OrderFac{

    @Override
    public HotspotOrder getOrder() {
        return new CQHotspot();
    }
}
