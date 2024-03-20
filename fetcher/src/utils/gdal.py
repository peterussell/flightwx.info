from osgeo import gdal

# $ gdal_translate -co "ZLEVEL=9" -of mobiles "~/charts/Chicago SEC.tif" ~/tiles/chicago_sec.mbtiles

def generate_mbtiles(in_path: str, out_path: str) -> None:
    print(f"Converting {in_path} to {out_path}")
    ds = gdal.Open(in_path)
    # ds = gdal.Translate(...) # working here
    print(ds)
