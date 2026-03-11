import ExcelJS from 'exceljs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, 'pdfs');

const MINT = '0D9488';
const CORAL = 'F97316';
const CHARCOAL = '1E293B';
const WHITE = 'FFFFFF';
const CREAM = 'FEFCE8';
const LIGHT_MINT = 'F0FDFA';

function styleHeader(row, color = MINT) {
  row.eachCell(c => {
    c.font = { bold: true, color: { argb: WHITE }, size: 11 };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: color } };
    c.alignment = { horizontal: 'center', vertical: 'middle', wrapText: true };
    c.border = {
      top: { style: 'thin', color: { argb: '999999' } },
      bottom: { style: 'thin', color: { argb: '999999' } },
      left: { style: 'thin', color: { argb: '999999' } },
      right: { style: 'thin', color: { argb: '999999' } },
    };
  });
  row.height = 28;
}

function styleCells(sheet, startRow, endRow) {
  for (let r = startRow; r <= endRow; r++) {
    const row = sheet.getRow(r);
    row.eachCell(c => {
      c.border = {
        top: { style: 'thin', color: { argb: 'DDDDDD' } },
        bottom: { style: 'thin', color: { argb: 'DDDDDD' } },
        left: { style: 'thin', color: { argb: 'DDDDDD' } },
        right: { style: 'thin', color: { argb: 'DDDDDD' } },
      };
      c.alignment = { vertical: 'middle', wrapText: true };
    });
    if (r % 2 === 0) {
      row.eachCell(c => {
        c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: LIGHT_MINT } };
      });
    }
  }
}

// ============ WORKBOOK 1: Donation Tracker & Earnings Log ============
async function createDonationTracker() {
  const wb = new ExcelJS.Workbook();
  wb.creator = 'Plasma Pay Calculator';

  // --- Tab 1: Monthly Tracker ---
  const ws1 = wb.addWorksheet('Monthly Tracker');
  ws1.columns = [
    { header: 'Date', key: 'date', width: 14 },
    { header: 'Center', key: 'center', width: 18 },
    { header: 'Base Pay', key: 'base', width: 12 },
    { header: 'Bonus', key: 'bonus', width: 12 },
    { header: 'Referral', key: 'referral', width: 12 },
    { header: 'Total', key: 'total', width: 12 },
    { header: 'Wait Time (min)', key: 'wait', width: 14 },
    { header: 'Donation Time (min)', key: 'donTime', width: 16 },
    { header: 'Mileage (round trip)', key: 'miles', width: 16 },
    { header: 'Notes', key: 'notes', width: 25 },
  ];
  styleHeader(ws1.getRow(1));

  // Sample rows
  const sampleDates = ['1/2/2026', '1/5/2026', '1/9/2026', '1/12/2026'];
  const centers = ['BioLife', 'CSL Plasma', 'Grifols', 'BioLife'];
  const basePays = [55, 50, 45, 55];
  const bonuses = [100, 0, 0, 0];
  sampleDates.forEach((d, i) => {
    ws1.addRow({
      date: d, center: centers[i], base: basePays[i], bonus: bonuses[i],
      referral: 0, total: { formula: `C${i+2}+D${i+2}+E${i+2}` },
      wait: 15, donTime: 45, miles: 12, notes: i === 0 ? 'New donor bonus!' : ''
    });
  });

  // Add 26 more empty rows for user
  for (let i = 0; i < 26; i++) {
    const r = 6 + i;
    ws1.addRow({ date: '', center: '', base: '', bonus: '', referral: '',
      total: { formula: `C${r}+D${r}+E${r}` }, wait: '', donTime: '', miles: '', notes: '' });
  }

  // Summary row
  const lastRow = 32;
  ws1.addRow([]);
  const sumRow = ws1.addRow(['TOTALS', '',
    { formula: `SUM(C2:C${lastRow})` },
    { formula: `SUM(D2:D${lastRow})` },
    { formula: `SUM(E2:E${lastRow})` },
    { formula: `SUM(F2:F${lastRow})` },
    { formula: `AVERAGE(G2:G${lastRow})` },
    { formula: `AVERAGE(H2:H${lastRow})` },
    { formula: `SUM(I2:I${lastRow})` },
    ''
  ]);
  styleHeader(sumRow, CORAL);
  styleCells(ws1, 2, lastRow);

  // Format currency
  ['C', 'D', 'E', 'F'].forEach(col => {
    ws1.getColumn(col).numFmt = '$#,##0.00';
  });

  // --- Tab 2: Monthly Summary ---
  const ws2 = wb.addWorksheet('Monthly Summary');
  ws2.columns = [
    { header: 'Month', key: 'month', width: 14 },
    { header: 'Donations', key: 'count', width: 12 },
    { header: 'Base Pay', key: 'base', width: 14 },
    { header: 'Bonuses', key: 'bonus', width: 14 },
    { header: 'Referrals', key: 'ref', width: 14 },
    { header: 'Total Earned', key: 'total', width: 14 },
    { header: 'Miles Driven', key: 'miles', width: 14 },
    { header: 'Mileage Deduction', key: 'deduction', width: 16 },
    { header: 'Net Income', key: 'net', width: 14 },
    { header: 'Avg $/Donation', key: 'avg', width: 14 },
  ];
  styleHeader(ws2.getRow(1));

  const months = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];
  months.forEach((m, i) => {
    const r = i + 2;
    ws2.addRow({
      month: m, count: i === 0 ? 4 : '', base: i === 0 ? 205 : '',
      bonus: i === 0 ? 100 : '', ref: '',
      total: { formula: `C${r}+D${r}+E${r}` },
      miles: i === 0 ? 48 : '',
      deduction: { formula: `G${r}*0.70` },
      net: { formula: `F${r}-H${r}` },
      avg: { formula: `IF(B${r}>0,F${r}/B${r},0)` }
    });
  });

  const annRow = ws2.addRow(['ANNUAL',
    { formula: 'SUM(B2:B13)' }, { formula: 'SUM(C2:C13)' },
    { formula: 'SUM(D2:D13)' }, { formula: 'SUM(E2:E13)' },
    { formula: 'SUM(F2:F13)' }, { formula: 'SUM(G2:G13)' },
    { formula: 'SUM(H2:H13)' }, { formula: 'SUM(I2:I13)' },
    { formula: 'IF(B14>0,F14/B14,0)' }
  ]);
  styleHeader(annRow, CORAL);
  styleCells(ws2, 2, 13);
  ['C', 'D', 'E', 'F', 'H', 'I', 'J'].forEach(col => {
    ws2.getColumn(col).numFmt = '$#,##0.00';
  });

  // --- Tab 3: Bonus Tracker ---
  const ws3 = wb.addWorksheet('Bonus Tracker');
  ws3.columns = [
    { header: 'Center', key: 'center', width: 18 },
    { header: 'Bonus Type', key: 'type', width: 20 },
    { header: 'Requirement', key: 'req', width: 30 },
    { header: 'Bonus Amount', key: 'amount', width: 14 },
    { header: 'Status', key: 'status', width: 14 },
    { header: 'Deadline', key: 'deadline', width: 14 },
    { header: 'Donations Done', key: 'done', width: 14 },
    { header: 'Donations Needed', key: 'needed', width: 16 },
    { header: 'Progress', key: 'progress', width: 12 },
  ];
  styleHeader(ws3.getRow(1));

  const bonusData = [
    ['BioLife', 'New Donor', '8 donations in 45 days', 900, 'Active', '2/15/2026', 4, 8],
    ['CSL Plasma', 'New Donor', '10 donations in 60 days', 1000, 'Active', '3/1/2026', 2, 10],
    ['Grifols', 'New Donor', '6 donations in 30 days', 700, 'Not Started', '', 0, 6],
    ['BioLife', 'Referral', 'Friend completes 2 donations', 100, 'Pending', '', 0, 2],
    ['CSL', 'Loyalty', 'Donate 8x in a month', 50, 'Active', '1/31/2026', 6, 8],
  ];
  bonusData.forEach((row, i) => {
    const r = i + 2;
    ws3.addRow([...row, { formula: `IF(H${r}>0,G${r}/H${r},0)` }]);
  });
  styleCells(ws3, 2, 6);
  ws3.getColumn('D').numFmt = '$#,##0.00';
  ws3.getColumn('I').numFmt = '0%';

  const fp = path.join(OUT, 'Plasma-Donation-Tracker.xlsx');
  await wb.xlsx.writeFile(fp);
  console.log('Created:', fp);
}

// ============ WORKBOOK 2: Mileage & Tax Deduction Log ============
async function createMileageTaxLog() {
  const wb = new ExcelJS.Workbook();
  wb.creator = 'Plasma Pay Calculator';

  // --- Tab 1: Mileage Log ---
  const ws1 = wb.addWorksheet('Mileage Log');
  ws1.columns = [
    { header: 'Date', key: 'date', width: 12 },
    { header: 'Purpose', key: 'purpose', width: 20 },
    { header: 'From', key: 'from', width: 18 },
    { header: 'To', key: 'to', width: 18 },
    { header: 'Start Odometer', key: 'start', width: 14 },
    { header: 'End Odometer', key: 'end', width: 14 },
    { header: 'Miles', key: 'miles', width: 10 },
    { header: 'IRS Rate', key: 'rate', width: 10 },
    { header: 'Deduction', key: 'deduction', width: 12 },
  ];
  styleHeader(ws1.getRow(1));

  // Sample rows
  const trips = [
    ['1/2/2026', 'Plasma donation', 'Home', 'BioLife', 45230, 45242, null, 0.70],
    ['1/5/2026', 'Plasma donation', 'Home', 'CSL Plasma', 45242, 45258, null, 0.70],
    ['1/9/2026', 'Plasma donation', 'Home', 'Grifols', 45258, 45270, null, 0.70],
    ['1/12/2026', 'Plasma donation', 'Home', 'BioLife', 45270, 45282, null, 0.70],
  ];
  trips.forEach((t, i) => {
    const r = i + 2;
    ws1.addRow([t[0], t[1], t[2], t[3], t[4], t[5],
      { formula: `F${r}-E${r}` }, t[7], { formula: `G${r}*H${r}` }
    ]);
  });

  for (let i = 0; i < 46; i++) {
    const r = 6 + i;
    ws1.addRow(['', 'Plasma donation', '', '', '', '',
      { formula: `F${r}-E${r}` }, 0.70, { formula: `G${r}*H${r}` }
    ]);
  }

  const lastR = 52;
  ws1.addRow([]);
  const sumR = ws1.addRow(['TOTALS', '', '', '', '', '',
    { formula: `SUM(G2:G${lastR})` }, '',
    { formula: `SUM(I2:I${lastR})` }
  ]);
  styleHeader(sumR, CORAL);
  styleCells(ws1, 2, lastR);
  ws1.getColumn('I').numFmt = '$#,##0.00';

  // --- Tab 2: Deduction Checklist ---
  const ws2 = wb.addWorksheet('Deduction Checklist');
  ws2.columns = [
    { header: 'Category', key: 'cat', width: 22 },
    { header: 'Deduction', key: 'ded', width: 35 },
    { header: 'Applies?', key: 'applies', width: 10 },
    { header: 'Amount', key: 'amount', width: 14 },
    { header: 'Notes', key: 'notes', width: 30 },
  ];
  styleHeader(ws2.getRow(1));

  const deductions = [
    ['Transportation', 'Mileage to/from center (IRS standard rate)'],
    ['Transportation', 'Parking at donation center'],
    ['Transportation', 'Tolls to/from center'],
    ['Transportation', 'Public transit fare to center'],
    ['Health & Nutrition', 'Supplements (iron, vitamin C, B12)'],
    ['Health & Nutrition', 'Pre-donation meals & hydration'],
    ['Health & Nutrition', 'Recovery snacks & drinks'],
    ['Health & Nutrition', 'Protein supplements'],
    ['Medical', 'Vein care supplies (compression, cream)'],
    ['Medical', 'Bandages & first aid supplies'],
    ['Medical', 'Bruise treatment supplies'],
    ['Supplies', 'Water bottles for hydration'],
    ['Supplies', 'Warm clothing for donation'],
    ['Supplies', 'Phone charger / entertainment'],
    ['Supplies', 'Insulated bag for snacks'],
    ['Administrative', 'Record keeping supplies'],
    ['Administrative', 'Tax preparation software'],
    ['Administrative', 'Accountant fees (plasma portion)'],
    ['Administrative', 'Phone usage (scheduling, tracking)'],
  ];
  deductions.forEach(d => ws2.addRow([d[0], d[1], '', '', '']));
  styleCells(ws2, 2, deductions.length + 1);

  const totRow = ws2.addRow(['', 'TOTAL DEDUCTIONS', '', { formula: `SUM(D2:D${deductions.length + 1})` }, '']);
  styleHeader(totRow, CORAL);
  ws2.getColumn('D').numFmt = '$#,##0.00';

  // --- Tab 3: Quarterly Tax Estimator ---
  const ws3 = wb.addWorksheet('Quarterly Tax Estimator');
  ws3.columns = [
    { header: '', key: 'label', width: 35 },
    { header: 'Q1', key: 'q1', width: 14 },
    { header: 'Q2', key: 'q2', width: 14 },
    { header: 'Q3', key: 'q3', width: 14 },
    { header: 'Q4', key: 'q4', width: 14 },
    { header: 'Annual', key: 'annual', width: 14 },
  ];
  styleHeader(ws3.getRow(1));

  const labels = [
    'Gross Plasma Income',
    'Mileage Deduction',
    'Other Deductions',
    'Net Taxable Income',
    '',
    'Federal Tax Rate (estimate)',
    'Federal Tax Owed',
    'Self-Employment Tax (15.3%)',
    'State Tax Rate (estimate)',
    'State Tax Owed',
    '',
    'TOTAL QUARTERLY TAX',
    '',
    'Payment Due Date',
  ];
  const dueQ = ['4/15/2026', '6/15/2026', '9/15/2026', '1/15/2027'];

  labels.forEach((label, i) => {
    const r = i + 2;
    if (label === '') { ws3.addRow([]); return; }
    if (label === 'Net Taxable Income') {
      ws3.addRow([label, { formula: `B2-B3-B4` }, { formula: `C2-C3-C4` },
        { formula: `D2-D3-D4` }, { formula: `E2-E3-E4` }, { formula: `SUM(B5:E5)` }]);
      return;
    }
    if (label === 'Federal Tax Owed') {
      ws3.addRow([label, { formula: `B5*B7` }, { formula: `C5*C7` },
        { formula: `D5*D7` }, { formula: `E5*E7` }, { formula: `SUM(B8:E8)` }]);
      return;
    }
    if (label === 'Self-Employment Tax (15.3%)') {
      ws3.addRow([label, { formula: `B5*0.153` }, { formula: `C5*0.153` },
        { formula: `D5*0.153` }, { formula: `E5*0.153` }, { formula: `SUM(B9:E9)` }]);
      return;
    }
    if (label === 'State Tax Owed') {
      ws3.addRow([label, { formula: `B5*B10` }, { formula: `C5*C10` },
        { formula: `D5*D10` }, { formula: `E5*E10` }, { formula: `SUM(B11:E11)` }]);
      return;
    }
    if (label === 'TOTAL QUARTERLY TAX') {
      ws3.addRow([label, { formula: `B8+B9+B11` }, { formula: `C8+C9+C11` },
        { formula: `D8+D9+D11` }, { formula: `E8+E9+E11` }, { formula: `SUM(B13:E13)` }]);
      return;
    }
    if (label === 'Federal Tax Rate (estimate)') {
      ws3.addRow([label, 0.12, 0.12, 0.12, 0.12, '']);
      return;
    }
    if (label === 'State Tax Rate (estimate)') {
      ws3.addRow([label, 0.05, 0.05, 0.05, 0.05, '']);
      return;
    }
    if (label === 'Gross Plasma Income') {
      ws3.addRow([label, 600, '', '', '', { formula: 'SUM(B2:E2)' }]);
      return;
    }
    if (label === 'Mileage Deduction') {
      ws3.addRow([label, 84, '', '', '', { formula: 'SUM(B3:E3)' }]);
      return;
    }
    if (label === 'Other Deductions') {
      ws3.addRow([label, 50, '', '', '', { formula: 'SUM(B4:E4)' }]);
      return;
    }
    if (label === 'Payment Due Date') {
      ws3.addRow([label, ...dueQ, '']);
      return;
    }
    ws3.addRow([label]);
  });

  styleCells(ws3, 2, 15);
  ['B', 'C', 'D', 'E', 'F'].forEach(col => {
    ws3.getColumn(col).numFmt = '$#,##0.00';
  });
  // Tax rates as percentages
  [7, 10].forEach(r => {
    ['B', 'C', 'D', 'E'].forEach(col => {
      const cell = ws3.getCell(`${col}${r}`);
      cell.numFmt = '0%';
    });
  });

  const fp = path.join(OUT, 'Plasma-Mileage-Tax-Log.xlsx');
  await wb.xlsx.writeFile(fp);
  console.log('Created:', fp);
}

// Run all
(async () => {
  await createDonationTracker();
  await createMileageTaxLog();
  console.log('All plasma spreadsheets generated!');
})();
