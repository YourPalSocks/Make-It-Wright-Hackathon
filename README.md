# Make-It-Wright-Hackathon
Make it Wright Hackathon Project

## Use Steps
### Manufacturing Tool
1. Run main.py
2. In the window popup, select the "Csv to Bartender Excel" button
3. Choose the CSV file to read
> The CSV file will be expected to follow the format of:
```Key,Value```

4. The tool will print the GTIN, Serial # (generated), Batch/Lot # (generated), Expiration Date, GS1 Element String, and SSCC
5. This database can be linked in Bartender to fill out various fields

### Bartender
1. Open the desired label template in Bartender.
2. Link the fields in the .xlsx (database) file created to those in the label template.
3. Create the RFID encodings using the Avery TDS Encoder/Decoder tool.
4. Once that is linked to the RFID object in template, the label is ready to print.

### Reader tool
# Tool to display the order information to the user
1. Run ReadFile.py
2. Choose the correct csv file to pull data from
3. Run gui.py to have the contents of order.txt displayed in a graphical interface
