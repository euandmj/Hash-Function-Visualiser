﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace Visualiser
{
    /// <summary>
    /// Interaction logic for FunctionWindow.xaml
    /// </summary>
    public partial class SHA1FunctionWindow : Window
    {
        private Int64 B, C, D, F;

        public SHA1FunctionWindow(int i, Int64[] buffers, Int64 F)
        {
            InitializeComponent();

            B = buffers[1];
            C = buffers[2];
            D = buffers[3];
            this.F = F;
           


            Initialise(i);
        }

        private void Initialise(int i)
        {
            bufferB.Text = Convert.ToString(B, 2);
            bufferC.Text = Convert.ToString(C, 2);
            bufferD.Text = Convert.ToString(D, 2);
            output.Text = Convert.ToString(F, 2);

            Image img = new Image();
            BitmapImage bmp = new BitmapImage();
            const string title = "Auxiliary Function ";
            // depending on i, load the correct function image
            if (i <= 19)
            {
                bmp.BeginInit();
                bmp.UriSource = new Uri("res/shaF.png", UriKind.Relative);
                bmp.EndInit();
                img.Source = bmp;
                img.Stretch = functionImage.Stretch;
                functionImage.Source = bmp;

                this.title.Content = title + "F";
            }
            else if(20 <= i && i <= 39)
            {
                bmp.BeginInit();
                bmp.UriSource = new Uri("res/shaG.png", UriKind.Relative);
                bmp.EndInit();
                img.Source = bmp;
                img.Stretch = functionImage.Stretch;
                functionImage.Source = bmp;


                this.title.Content = title + "G";
            }
            else if(40 <= i && i <= 59)
            {
                bmp.BeginInit();
                bmp.UriSource = new Uri("res/shaH.png", UriKind.Relative);
                bmp.EndInit();
                img.Source = bmp;
                img.Stretch = functionImage.Stretch;
                functionImage.Source = bmp;


                this.title.Content = title + "H";
            }
            else if(60 <= i && i <= 79)
            {
                bmp.BeginInit();
                bmp.UriSource = new Uri("res/shaG.png", UriKind.Relative);
                bmp.EndInit();
                img.Source = bmp;
                img.Stretch = functionImage.Stretch;
                functionImage.Source = bmp;


                this.title.Content = title + "I";
            }
        }
    }
}
