public class CDOrderFac implements OrderFac{
    public HotspotOrder getOrder(){
        return new CDHotspot();
    }
}
