# Converting DHL internation shipping PDF to a single page

When shipping internationally with DHL, I get a 2-page PDF document, where one half of each page needs to go on the package, and the other half into the trash. I'd much rather just have a single page that I need to print. This is rather hard to achieve manually, so I ended up writing a little script to achieve this for me.

## Setup
```
git clone https://github.com/tiefpunkt/dhl_onepager.git
cd dhl_onepager
python3 -mvenv env
./env/bin/pip install -r requirements.txt
```

## Operation
```
./env/bin/python3 dhl_onepager.py DHL-Paketmarke_blablabla.pdf
```

This will create a DHL-Paketmarke_blablabla_onepage.pdf PDF file, which is only a single page long.
