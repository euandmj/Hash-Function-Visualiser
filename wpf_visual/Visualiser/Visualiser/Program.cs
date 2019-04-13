using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace Visualiser
{
    class Program
    {
        [STAThread]
        public static void Main(string[] args)
        {
            //var foo = new SHA1MainWindow();
            //foo.ShowDialog();

            if (args.Length == 0)
                throw new NotImplementedException("launch visualiser with hash type args");

            Window window = null;


            switch (args[0])
            {
                case "md5":
                    window = new MD5MainWindow();
                    break;
                case "sha1":
                    window = new SHA1MainWindow();
                    break;
            }
            window.ShowDialog();
        }
    }
}
