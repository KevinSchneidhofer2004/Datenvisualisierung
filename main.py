from file_downloader import FileDownloader

file_downloader = FileDownloader('https://service.stmk.gv.at/ogd/OGD_Data_ABT17/statistik/SCHULE/STMK_202122_SCHUELER.csv')

file_downloader.download()
file_downloader.save_data('save_data.csv')
file_downloader.visualize()
