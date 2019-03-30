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
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Web.Script.Serialization;
using System.IO;

namespace Visualiser
{
    struct Loop
    {
        public Int64[] Buffers;
        public Int64 F;
        public Int64 M;
        public Int64 S;
        public Int64 T;
        public int I;


        public string GetBuffer(int n)
        {
            return Buffers[n].ToString();
        }
    }
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        const string filename = "curr_loop.json";
        private readonly Loop Loop; 

        public MainWindow()
        {
            InitializeComponent();
            string raw = string.Empty;
            // serialise the file
            using (var reader = new StreamReader(filename))
            {
                raw = reader.ReadToEnd();
            }
            Loop = new JavaScriptSerializer().Deserialize<Loop>(raw);



            Initialise();
        }

        private void Initialise()
        {
            BufferA.Text = Loop.GetBuffer(0);
            BufferB.Text = Loop.GetBuffer(1);
            BufferC.Text = Loop.GetBuffer(2);
            BufferD.Text = Loop.GetBuffer(3);

        }

        private void Rectangle_MouseDown(object sender, MouseButtonEventArgs e)
        {
            FunctionWindow window = new FunctionWindow(Loop.I, Loop.Buffers, Loop.F);
            window.ShowDialog();
        }

        private void Mblock_click_MouseDown(object sender, MouseButtonEventArgs e)
        {
            MessageBox.Show(Loop.M.ToString());
        }

        private void Tblock_click_MouseDown(object sender, MouseButtonEventArgs e)
        {
            MessageBox.Show(Loop.T.ToString());
        }
    }
}