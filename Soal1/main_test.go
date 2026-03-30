package main

import (
	"fmt"
	"strconv"
	"testing"
	"time"
)

func parseDate(dateStr, layout string) time.Time {
	t, _ := time.Parse(layout, dateStr)
	return t
}

func TestCalculateLoyalty_ReportStyle(t *testing.T) {
	layout := "2006-01-02"

	tests := []struct {
		name              string
		transactions      []Transaction
		expectedPoints    int
		expectedDiscount  DiscountTier
		expectedHighValue int
	}{
		{
			name: "Mix transaksi hari kerja dan weekend",
			transactions: []Transaction{
				{ID: "T1", Amount: 600000, Date: parseDate("2026-03-28", layout), Status: StatusSuccess}, // Sabtu, >500k
				{ID: "T2", Amount: 300000, Date: parseDate("2026-03-29", layout), Status: StatusSuccess}, // Minggu, <500k
				{ID: "T3", Amount: 700000, Date: parseDate("2026-03-30", layout), Status: StatusSuccess}, // Senin, >500k
				{ID: "T4", Amount: 200000, Date: parseDate("2026-03-31", layout), Status: StatusFailed},  // gagal
				{ID: "T5", Amount: 100000, Date: parseDate("2026-04-01", layout), Status: StatusSuccess}, // Rabu, <500k
			},
			expectedPoints:    13,
			expectedDiscount:  TierRegular,
			expectedHighValue: 2,
		},
		{
			name: "Transaksi banyak hingga SUPER_VIP",
			transactions: func() []Transaction {
				var txs []Transaction
				for i := 0; i < 11; i++ {
					txs = append(txs, Transaction{
						ID:     "HVP" + strconv.Itoa(i),
						Amount: 600000,
						Date:   parseDate("2026-03-30", layout),
						Status: StatusSuccess,
					})
				}
				return txs
			}(),
			expectedPoints:    55,
			expectedDiscount:  TierSuperVIP,
			expectedHighValue: 11,
		},
		{
			name: "Tidak ada transaksi berhasil",
			transactions: []Transaction{
				{ID: "F1", Amount: 100000, Date: parseDate("2026-03-30", layout), Status: StatusFailed},
				{ID: "F2", Amount: 700000, Date: parseDate("2026-03-28", layout), Status: StatusFailed},
			},
			expectedPoints:    0,
			expectedDiscount:  TierNone,
			expectedHighValue: 0,
		},
	}

	fmt.Println("=================================================================")
	fmt.Println("| No | Skenario                               | Total Points | Max Discount | High Value Tx | PASS |")
	fmt.Println("=================================================================")

	for i, tt := range tests {
		result := CalculateLoyalty(tt.transactions)

		pass := result.TotalPoints == tt.expectedPoints &&
			result.MaxDiscount == tt.expectedDiscount &&
			result.HighValueTransactionCount == tt.expectedHighValue

		fmt.Printf("| %2d | %-38s | %12d | %-12s | %13d | %-4v |\n",
			i+1,
			tt.name,
			result.TotalPoints,
			result.MaxDiscount,
			result.HighValueTransactionCount,
			pass,
		)

		if !pass {
			t.Errorf("Test %s gagal", tt.name)
		}
	}

	fmt.Println("=================================================================")
}